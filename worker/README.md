# Iron Custom Motors — Reviews Worker

Cloudflare Worker that proxies the Google Places API (New) and caches the result for 24 hours. Frontend calls this endpoint instead of Google directly so the API key stays on the server side.

## Architecture

```
Browser → Cloudflare Worker (cached 24h) → Google Places API
                ↓
         Returns JSON: rating, total, reviews[]
```

- **Cache:** a deterministic `caches.default` key, with response headers
  `max-age=86400` (24 hours) and `stale-while-revalidate=90000`.
- **Failure behavior:** a cache hit returns the cached response. A cache miss
  calls Google; a network or upstream API failure returns HTTP 502. The Worker
  does not implement stale-body recovery or background revalidation. The
  website separately retains static review cards and a committed snapshot.
- **Field mask:** the explicit fields in `reviews.js` request the aggregate
  and Google-provided reviews. Billing depends on the current Google SKU and
  account configuration; this repository does not enforce a daily budget.

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
# paste the rotated, API-restricted Google Places API key when prompted
wrangler deploy
```

If a Google API key was ever committed to this public repository, revoke it in
Google Cloud before relying on this Worker. Removing the value from this file
does not remove it from Git history.

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

The secret command creates and deploys an updated Worker version. Verify the
public endpoint after the update; never print the secret value.

## Cache refresh and request volume

A new Google request is made when the regional Cache API lookup misses.
The cache can be evicted, regions maintain separate entries, and simultaneous
misses can issue concurrent requests. Redeploying does not guarantee that this
fixed cache key is purged. There is no force-refresh endpoint.

Use the Google Cloud usage, quota and billing controls to measure and constrain
actual API usage. Do not infer a fixed daily request count or free allowance
from the cache TTL. Wait for expiry for an ordinary content refresh; change
cache behavior only as an explicitly reviewed Worker change.

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
# local mode needs GOOGLE_API_KEY in gitignored .dev.vars or an approved secret source
```
