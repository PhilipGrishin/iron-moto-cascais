const ALLOWED_ORIGINS = new Set([
  "https://ironcustommotors.com",
  "https://www.ironcustommotors.com",
]);
const EVENT_TYPES = ["whatsapp", "tel", "form_submit", "form_view"];
const EVENT_TYPE_SET = new Set(EVENT_TYPES);
const LANGS = new Set(["en", "pt", "ru", "uk"]);
const MAX_STATS_DAYS = 90;
const RATE_LIMIT_PER_MINUTE = 120;
const COUNTER_TTL_SECONDS = 400 * 24 * 60 * 60;
const TEST_PAGE = "/**test**/";

const rateBuckets = new Map();
const pendingWrites = new Map();

function jsonResponse(body, status = 200, origin = null, extraHeaders = {}) {
  const headers = new Headers({
    "content-type": "application/json; charset=utf-8",
    "cache-control": "no-store",
    "referrer-policy": "no-referrer",
    ...extraHeaders,
  });
  if (origin && ALLOWED_ORIGINS.has(origin)) {
    headers.set("access-control-allow-origin", origin);
    headers.set("vary", "Origin");
  }
  return new Response(JSON.stringify(body), { status, headers });
}

function rejectOrigin(origin) {
  return jsonResponse({ error: "Origin is not allowed" }, 403);
}

function dateInLisbon(date = new Date()) {
  const parts = new Intl.DateTimeFormat("en-CA", {
    timeZone: "Europe/Lisbon",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).formatToParts(date);
  const value = Object.fromEntries(parts.map(({ type, value: item }) => [type, item]));
  return `${value.year}-${value.month}-${value.day}`;
}

function dateRange(days) {
  const [year, month, day] = dateInLisbon().split("-").map(Number);
  const end = Date.UTC(year, month - 1, day);
  return Array.from({ length: days }, (_, offset) =>
    new Date(end - offset * 86400000).toISOString().slice(0, 10)
  ).reverse();
}

function languageForPath(page) {
  const match = page.match(/^\/(pt|ru|uk)(?:\/|$)/);
  return match ? match[1] : "en";
}

function validPage(page) {
  return typeof page === "string"
    && page.startsWith("/")
    && page.length <= 512
    && !page.includes("?")
    && !page.includes("#")
    && !/[\u0000-\u001f\u007f]/.test(page);
}

function normalizedRef(ref) {
  if (!ref) return "direct";
  if (typeof ref !== "string" || ref.length > 512) return null;
  try {
    const host = new URL(ref).hostname.toLowerCase();
    if (!host) return "direct";
    return host === "ironcustommotors.com" || host === "www.ironcustommotors.com"
      ? "internal"
      : host;
  } catch {
    return ref === "direct" || ref === "internal" ? ref : null;
  }
}

function encodePage(page) {
  const bytes = new TextEncoder().encode(page);
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
}

function rateLimited() {
  const bucket = Math.floor(Date.now() / 60000);
  const previousBucket = bucket - 1;
  for (const key of rateBuckets.keys()) {
    if (key < previousBucket) rateBuckets.delete(key);
  }
  const count = (rateBuckets.get(bucket) || 0) + 1;
  rateBuckets.set(bucket, count);
  return count > RATE_LIMIT_PER_MINUTE;
}

function enqueueIncrement(kv, key, metadata) {
  const previous = pendingWrites.get(key) || Promise.resolve();
  const next = previous.then(async () => {
    const current = Number(await kv.get(key)) || 0;
    const count = current + 1;
    await kv.put(key, String(count), {
      expirationTtl: COUNTER_TTL_SECONDS,
      metadata: { ...metadata, count },
    });
  }).finally(() => {
    if (pendingWrites.get(key) === next) pendingWrites.delete(key);
  });
  pendingWrites.set(key, next);
  return next;
}

async function recordEvent(request, env, ctx, origin) {
  if (!origin || !ALLOWED_ORIGINS.has(origin)) return rejectOrigin(origin);
  if (!env.LEAD_COUNTS) return jsonResponse({ error: "KV binding is unavailable" }, 503, origin);
  if (rateLimited()) {
    return jsonResponse({ error: "Rate limit exceeded" }, 429, origin, { "retry-after": "60" });
  }
  const length = Number(request.headers.get("content-length") || 0);
  if (length > 4096) return jsonResponse({ error: "Request body is too large" }, 413, origin);

  let payload;
  try {
    payload = await request.json();
  } catch {
    return jsonResponse({ error: "Request body must be valid JSON" }, 400, origin);
  }
  if (!payload || typeof payload !== "object" || Array.isArray(payload)) {
    return jsonResponse({ error: "Request body must be a JSON object" }, 400, origin);
  }
  const { type, page, lang, ref } = payload;
  if (!EVENT_TYPE_SET.has(type)) {
    return jsonResponse({ error: `type must be one of: ${EVENT_TYPES.join(", ")}` }, 400, origin);
  }
  if (!validPage(page)) {
    return jsonResponse({ error: "page must be a path without a query or fragment" }, 400, origin);
  }
  if (!LANGS.has(lang) || languageForPath(page) !== lang) {
    return jsonResponse({ error: "lang must match the page path" }, 400, origin);
  }
  if (normalizedRef(ref) === null) {
    return jsonResponse({ error: "ref must be a URL hostname source or direct/internal" }, 400, origin);
  }

  const date = dateInLisbon();
  const prefix = page === TEST_PAGE ? "test:d" : "d";
  const writes = [
    enqueueIncrement(env.LEAD_COUNTS, `${prefix}:${date}:t:${type}`, {
      scope: "type", date, type,
    }),
    enqueueIncrement(env.LEAD_COUNTS, `${prefix}:${date}:l:${lang}:t:${type}`, {
      scope: "language", date, lang, type,
    }),
    enqueueIncrement(env.LEAD_COUNTS, `${prefix}:${date}:p:${encodePage(page)}:t:${type}`, {
      scope: "page", date, page, lang, type,
    }),
  ];
  const completed = Promise.all(writes);
  ctx.waitUntil(completed);
  await completed;
  return jsonResponse({ ok: true }, 202, origin);
}

function emptyTypes() {
  return Object.fromEntries(EVENT_TYPES.map((type) => [type, 0]));
}

function safeEqual(left, right) {
  if (typeof left !== "string" || typeof right !== "string") return false;
  const length = Math.max(left.length, right.length);
  let diff = left.length ^ right.length;
  for (let index = 0; index < length; index += 1) {
    diff |= (left.charCodeAt(index) || 0) ^ (right.charCodeAt(index) || 0);
  }
  return diff === 0;
}

async function listDay(kv, date, prefix = "d") {
  const keys = [];
  let cursor;
  do {
    const result = await kv.list({ prefix: `${prefix}:${date}:`, cursor });
    keys.push(...result.keys);
    cursor = result.list_complete ? undefined : result.cursor;
  } while (cursor);
  return keys;
}

async function readStats(request, env, origin) {
  if (origin && !ALLOWED_ORIGINS.has(origin)) return rejectOrigin(origin);
  if (!env.STATS_TOKEN || !env.LEAD_COUNTS) {
    return jsonResponse({ error: "Worker is not configured" }, 503, origin);
  }
  const url = new URL(request.url);
  if (!safeEqual(url.searchParams.get("token"), env.STATS_TOKEN)) {
    return jsonResponse({ error: "Unauthorized" }, 401, origin);
  }
  const days = Number(url.searchParams.get("days") || 28);
  if (!Number.isInteger(days) || days < 1 || days > MAX_STATS_DAYS) {
    return jsonResponse({ error: `days must be an integer from 1 to ${MAX_STATS_DAYS}` }, 400, origin);
  }
  const includeTests = ["1", "true"].includes(
    (url.searchParams.get("includeTests") || "").toLowerCase(),
  );

  const dates = dateRange(days);
  const totals = emptyTypes();
  const pageMap = new Map();
  const languageMap = new Map();
  const byDay = [];

  for (const date of dates) {
    const dayTypes = emptyTypes();
    const keys = await listDay(env.LEAD_COUNTS, date);
    if (includeTests) keys.push(...await listDay(env.LEAD_COUNTS, date, "test:d"));
    for (const key of keys) {
      const metadata = key.metadata || {};
      const count = Number(metadata.count ?? await env.LEAD_COUNTS.get(key.name)) || 0;
      if (!EVENT_TYPE_SET.has(metadata.type)) continue;
      if (metadata.scope === "type") {
        totals[metadata.type] += count;
        dayTypes[metadata.type] += count;
      } else if (metadata.scope === "language" && LANGS.has(metadata.lang)) {
        const row = languageMap.get(metadata.lang) || { lang: metadata.lang, byType: emptyTypes() };
        row.byType[metadata.type] += count;
        languageMap.set(metadata.lang, row);
      } else if (metadata.scope === "page" && validPage(metadata.page)) {
        const row = pageMap.get(metadata.page) || {
          page: metadata.page,
          lang: metadata.lang,
          byType: emptyTypes(),
        };
        row.byType[metadata.type] += count;
        pageMap.set(metadata.page, row);
      }
    }
    byDay.push({
      date,
      total: Object.values(dayTypes).reduce((sum, count) => sum + count, 0),
      byType: dayTypes,
    });
  }

  const withTotal = (row) => ({
    ...row,
    total: Object.values(row.byType).reduce((sum, count) => sum + count, 0),
  });
  const pages = [...pageMap.values()].map(withTotal)
    .sort((left, right) => right.total - left.total || left.page.localeCompare(right.page));
  const languages = [...languageMap.values()].map(withTotal)
    .sort((left, right) => right.total - left.total || left.lang.localeCompare(right.lang));

  return jsonResponse({
    generatedAt: new Date().toISOString(),
    days,
    includeTests,
    from: dates[0],
    to: dates.at(-1),
    totals,
    pages,
    languages,
    byDay,
  }, 200, origin);
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const origin = request.headers.get("origin");

    if (request.method === "OPTIONS") {
      if (!origin || !ALLOWED_ORIGINS.has(origin)) return rejectOrigin(origin);
      return new Response(null, {
        status: 204,
        headers: {
          "access-control-allow-origin": origin,
          "access-control-allow-methods": "POST, GET, OPTIONS",
          "access-control-allow-headers": "content-type",
          "access-control-max-age": "86400",
          "cache-control": "no-store",
          vary: "Origin",
        },
      });
    }
    if (url.pathname === "/event" && request.method === "POST") {
      return recordEvent(request, env, ctx, origin);
    }
    if (url.pathname === "/stats" && request.method === "GET") {
      return readStats(request, env, origin);
    }
    return jsonResponse({ error: "Not found" }, 404, origin);
  },
};
