/**
 * Iron Custom Motors — Google Reviews proxy
 * Cloudflare Worker that caches Google Places API (New) responses for 24h
 *
 * Free tier: 100k req/day. With 24h cache only 1-2 actual API calls/day.
 *
 * Deploy:
 *   cd worker && wrangler deploy
 *
 * Set secret:
 *   wrangler secret put GOOGLE_API_KEY
 *
 * Endpoint:  GET https://icm-reviews.<account>.workers.dev/
 *   Returns JSON: { name, rating, total, reviews: [...], fetchedAt }
 */

const PLACE_ID = 'ChIJ-5VQL2bPHg0R-Oj5dD0Ojhk';
const FIELD_MASK = [
  'displayName',
  'rating',
  'userRatingCount',
  'reviews.rating',
  'reviews.text',
  'reviews.originalText',
  'reviews.authorAttribution',
  'reviews.relativePublishTimeDescription',
  'reviews.publishTime',
  'reviews.googleMapsUri'
].join(',');

// 24h browser/edge cache
const MAX_AGE = 60 * 60 * 24;
// 25h stale-while-revalidate (so site stays fast even if API slow)
const SWR = 60 * 60 * 25;

const ALLOWED_ORIGINS = [
  'https://ironcustommotors.com',
  'https://www.ironcustommotors.com',
  // GitHub Pages preview
  'https://philipgrishin.github.io'
];

function corsHeaders(origin) {
  const allow = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    'Access-Control-Allow-Origin': allow,
    'Access-Control-Allow-Methods': 'GET, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
    'Vary': 'Origin'
  };
}

function reviewTimestamp(review) {
  const time = Date.parse(review?.publishedAt || review?.publishTime || '');
  return Number.isFinite(time) ? time : 0;
}

function sortReviewsNewestFirst(reviews) {
  return [...reviews].sort((a, b) => {
    const byDate = reviewTimestamp(b) - reviewTimestamp(a);
    if (byDate !== 0) return byDate;
    const byRating = (b.rating || 0) - (a.rating || 0);
    if (byRating !== 0) return byRating;
    return String(b.text || '').length - String(a.text || '').length;
  });
}

export default {
  async fetch(request, env, ctx) {
    const origin = request.headers.get('Origin') || '';

    // CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: corsHeaders(origin) });
    }
    if (request.method !== 'GET') {
      return new Response('Method not allowed', { status: 405, headers: corsHeaders(origin) });
    }

    // Build deterministic cache key (independent of request URL specifics)
    const cacheKey = new Request('https://icm-reviews-cache/v1/place', { method: 'GET' });
    const cache = caches.default;

    // Try cache first
    let cached = await cache.match(cacheKey);
    if (cached) {
      return withCors(cached, origin);
    }

    // Cache miss → call Google Places API (New)
    if (!env.GOOGLE_API_KEY) {
      return jsonResp({ error: 'GOOGLE_API_KEY not configured' }, 500, origin);
    }

    // No languageCode → Google returns each review in the original language the author wrote it in.
    // We surface r.originalText (real author text) instead of r.text (which would be a Google machine-translation).
    const apiUrl = `https://places.googleapis.com/v1/places/${PLACE_ID}`;
    let apiResp;
    try {
      apiResp = await fetch(apiUrl, {
        headers: {
          'X-Goog-Api-Key': env.GOOGLE_API_KEY,
          'X-Goog-FieldMask': FIELD_MASK
        }
      });
    } catch (err) {
      return jsonResp({ error: 'fetch_failed', message: String(err) }, 502, origin);
    }

    if (!apiResp.ok) {
      const text = await apiResp.text();
      return jsonResp({ error: 'api_error', status: apiResp.status, body: text.slice(0, 500) }, 502, origin);
    }

    const raw = await apiResp.json();

    // Map to clean schema and surface the newest Google-provided reviews first.
    const reviews = sortReviewsNewestFirst((raw.reviews || []).map(r => ({
      author: r.authorAttribution?.displayName || 'Anonymous',
      avatar: r.authorAttribution?.photoUri || null,
      profileUrl: r.authorAttribution?.uri || null,
      rating: typeof r.rating === 'number' ? r.rating : 5,
      // Prefer originalText (real author wording) over text (which is Google's translation when languageCode is set).
      text: r.originalText?.text || r.text?.text || '',
      lang: r.originalText?.languageCode || r.text?.languageCode || null,
      when: r.relativePublishTimeDescription || '',
      publishedAt: r.publishTime || null,
      url: r.googleMapsUri || null
    }))).slice(0, 5);

    const payload = {
      name: raw.displayName?.text || 'Iron Custom Motors',
      rating: typeof raw.rating === 'number' ? raw.rating : null,
      total: raw.userRatingCount || 0,
      reviews,
      fetchedAt: new Date().toISOString()
    };

    const response = new Response(JSON.stringify(payload), {
      status: 200,
      headers: {
        'Content-Type': 'application/json; charset=utf-8',
        'Cache-Control': `public, max-age=${MAX_AGE}, stale-while-revalidate=${SWR}`,
        ...corsHeaders(origin)
      }
    });

    // Store in edge cache (separate from response we return — must clone)
    ctx.waitUntil(cache.put(cacheKey, response.clone()));

    return response;
  }
};

function withCors(response, origin) {
  const r = new Response(response.body, response);
  Object.entries(corsHeaders(origin)).forEach(([k, v]) => r.headers.set(k, v));
  return r;
}

function jsonResp(obj, status, origin) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      ...corsHeaders(origin)
    }
  });
}
