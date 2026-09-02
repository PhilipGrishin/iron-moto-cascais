import assert from "node:assert/strict";
import test from "node:test";

import worker from "./worker.mjs";

class MemoryKV {
  constructor() {
    this.values = new Map();
    this.metadata = new Map();
  }

  async get(key) {
    return this.values.get(key) ?? null;
  }

  async put(key, value, options = {}) {
    this.values.set(key, value);
    this.metadata.set(key, options.metadata || null);
  }

  async list({ prefix = "" }) {
    return {
      keys: [...this.values.keys()]
        .filter((key) => key.startsWith(prefix))
        .sort()
        .map((name) => ({ name, metadata: this.metadata.get(name) })),
      list_complete: true,
      cursor: "",
    };
  }
}

function environment() {
  return { LEAD_COUNTS: new MemoryKV(), STATS_TOKEN: "test-stats-token" };
}

function context() {
  return { waitUntil(promise) { return promise; } };
}

function eventRequest(payload, origin = "https://ironcustommotors.com") {
  return new Request("https://icm-leads.example/event", {
    method: "POST",
    headers: { origin, "content-type": "text/plain;charset=UTF-8" },
    body: JSON.stringify(payload),
  });
}

test("records all supported lead types and reports totals", async () => {
  const env = environment();
  const events = [
    { type: "whatsapp", page: "/pricing/", lang: "en", ref: "https://google.com/search?q=private" },
    { type: "tel", page: "/pt/contact/", lang: "pt", ref: "internal" },
    { type: "form_view", page: "/ru/", lang: "ru", ref: "direct" },
    { type: "form_submit", page: "/uk/contact/", lang: "uk", ref: "direct" },
  ];
  for (const payload of events) {
    const response = await worker.fetch(eventRequest(payload), env, context());
    assert.equal(response.status, 202);
    assert.equal(response.headers.get("set-cookie"), null);
  }
  for (const type of ["whatsapp", "tel", "form_submit", "form_view"]) {
    const response = await worker.fetch(eventRequest({
      type, page: "/**test**/", lang: "en", ref: "direct",
    }), env, context());
    assert.equal(response.status, 202);
  }

  const response = await worker.fetch(
    new Request("https://icm-leads.example/stats?days=7&token=test-stats-token"),
    env,
    context(),
  );
  assert.equal(response.status, 200);
  const stats = await response.json();
  assert.deepEqual(stats.totals, {
    whatsapp: 1,
    tel: 1,
    form_submit: 1,
    form_view: 1,
  });
  assert.equal(stats.pages.length, 4);
  assert.deepEqual(stats.languages.map(({ lang }) => lang).sort(), ["en", "pt", "ru", "uk"]);
  assert.equal(stats.byDay.reduce((sum, row) => sum + row.total, 0), 4);
  assert.equal(stats.includeTests, false);
  assert.equal(stats.pages.some(({ page }) => page === "/**test**/"), false);

  const acceptanceResponse = await worker.fetch(
    new Request("https://icm-leads.example/stats?days=7&includeTests=1&token=test-stats-token"),
    env,
    context(),
  );
  const acceptanceStats = await acceptanceResponse.json();
  assert.equal(acceptanceStats.includeTests, true);
  assert.deepEqual(acceptanceStats.totals, {
    whatsapp: 2,
    tel: 2,
    form_submit: 2,
    form_view: 2,
  });
  assert.equal(
    acceptanceStats.pages.find(({ page }) => page === "/**test**/")?.total,
    4,
  );

  const persisted = JSON.stringify([
    ...env.LEAD_COUNTS.values.entries(),
    ...env.LEAD_COUNTS.metadata.entries(),
  ]);
  assert.doesNotMatch(persisted, /private|google\.com|user-agent|127\.0\.0\.1/i);
  assert.match(persisted, /test:d:/);
});

test("rejects missing token and untrusted origins", async () => {
  const env = environment();
  const unauthorized = await worker.fetch(
    new Request("https://icm-leads.example/stats?days=7"),
    env,
    context(),
  );
  assert.equal(unauthorized.status, 401);

  const forbidden = await worker.fetch(
    eventRequest(
      { type: "tel", page: "/", lang: "en", ref: "direct" },
      "https://example.com",
    ),
    env,
    context(),
  );
  assert.equal(forbidden.status, 403);
  assert.equal(forbidden.headers.get("access-control-allow-origin"), null);
});

test("handles allowed and rejected preflight requests", async () => {
  const env = environment();
  const allowed = await worker.fetch(new Request("https://icm-leads.example/event", {
    method: "OPTIONS",
    headers: { origin: "https://www.ironcustommotors.com" },
  }), env, context());
  assert.equal(allowed.status, 204);
  assert.equal(allowed.headers.get("access-control-allow-origin"), "https://www.ironcustommotors.com");

  const rejected = await worker.fetch(new Request("https://icm-leads.example/event", {
    method: "OPTIONS",
    headers: { origin: "https://attacker.example" },
  }), env, context());
  assert.equal(rejected.status, 403);
});

test("validates page language and event type", async () => {
  const env = environment();
  const languageMismatch = await worker.fetch(eventRequest({
    type: "whatsapp", page: "/pt/contact/", lang: "en", ref: "direct",
  }), env, context());
  assert.equal(languageMismatch.status, 400);

  const unknownType = await worker.fetch(eventRequest({
    type: "email", page: "/", lang: "en", ref: "direct",
  }), env, context());
  assert.equal(unknownType.status, 400);
});

test("applies an anonymous per-isolate rate limit", async () => {
  const env = environment();
  let response;
  for (let index = 0; index < 121; index += 1) {
    response = await worker.fetch(eventRequest({
      type: "tel", page: "/contact/", lang: "en", ref: "direct",
    }), env, context());
  }
  assert.equal(response.status, 429);
  assert.equal(response.headers.get("retry-after"), "60");
  assert.equal(response.headers.get("set-cookie"), null);
});
