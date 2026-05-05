# Iron Custom Motors — Reviews Worker

Cloudflare Worker that proxies the Google Places API (New) and caches the result for 24 hours. Frontend calls this endpoint instead of Google directly so the API key stays on the server side.

## Architecture

```
Browser → Cloudflare Worker (cached 24h) → Google Places API
                ↓
         Returns JSON: rating, total, reviews[]
```

- **Cache:** Cloudflare edge cache, `s-maxage=86400` (24h) + `stale-while-revalidate=90000` (25h).
- **Real Google API hits:** ≤2/day per Cloudflare region (well under your 10–20/day budget).
- **Cost protection:** if cache miss + Google fails, returns last cached body (SWR).
- **Field mask:** explicit list (`displayName, rating, userRatingCount, reviews.*`) — no `*` wildcard, no extra billed fields.

## One-time setup

Install the Cloudflare CLI:

```bash
npm install -g wrangler
```

Login (opens browser):

```bash
wrangler login
```

## Deploy

From the project root:

```bash
cd worker
wrangler secret put GOOGLE_API_KEY
# paste: AIzaSyBxhQ4qdihRNVcYxPnsHaew5rgfWmoUmS0
wrangler deploy
```

Wrangler will print the Worker URL, e.g.:

```
https://icm-reviews.<your-account>.workers.dev
```

Test it:

```bash
curl https://icm-reviews.<your-account>.workers.dev/
```

You should get JSON with `rating`, `total`, `reviews[]`.

## Hook to ironcustommotors.com (recommended)

Two options:

### Option A — Custom subdomain (simpler)

In **Cloudflare DNS** for `ironcustommotors.com`, add:

```
CNAME  reviews   icm-reviews.<your-account>.workers.dev   Proxied
```

Then in `wrangler.toml`:

```toml
[[routes]]
pattern = "reviews.ironcustommotors.com/*"
zone_name = "ironcustommotors.com"
```

Re-deploy: `wrangler deploy`. Endpoint becomes `https://reviews.ironcustommotors.com/`.

### Option B — Same-origin path (keeps everything on apex)

In `wrangler.toml`:

```toml
[[routes]]
pattern = "ironcustommotors.com/api/reviews*"
zone_name = "ironcustommotors.com"
```

Re-deploy. Endpoint becomes `https://ironcustommotors.com/api/reviews` — looks like part of the site, not a separate service. **Caveat:** you have to make sure GitHub Pages doesn't try to handle that path. Since GH Pages 404 on that path, Cloudflare Worker route takes precedence, and you're good.

## Update API key

```bash
cd worker
wrangler secret put GOOGLE_API_KEY
# paste new key
```

No re-deploy needed — secrets reload automatically.

## Force cache refresh (testing)

The Worker only caches successful 200 responses. To force a refresh, re-deploy:

```bash
wrangler deploy
```

Or call from a different Cloudflare region to bypass the cached edge node.

## Daily request budget

| Cache state | Google API hit |
|---|---|
| Edge cache hit (almost all visits) | 0 |
| Edge cache miss after 24h | 1 per region |
| Cold worker boot | 1 |

With ≤6 Cloudflare regions serving your audience, you'll see **2–10 Google API calls/day** — within the documented free Places API quota.

## Response shape

```json
{
  "name": "Iron Custom Motors",
  "rating": 4.9,
  "total": 47,
  "reviews": [
    {
      "author": "James M.",
      "avatar": "https://...",
      "profileUrl": "https://...",
      "rating": 5,
      "text": "Brought my BMW R nineT...",
      "lang": "en",
      "when": "2 weeks ago",
      "publishedAt": "2026-04-18T12:34:56Z",
      "url": "https://www.google.com/maps/reviews/..."
    }
  ],
  "fetchedAt": "2026-05-05T12:00:00Z"
}
```

## Local development

```bash
cd worker
wrangler dev
# opens http://localhost:8787
# uses production Google API key set via `wrangler secret put`
```
