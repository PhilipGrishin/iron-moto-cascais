# Iron Custom Motors Lead Beacon Worker

`icm-leads` records anonymous lead-intent counters for the static website. It
does not use cookies and never reads or stores IP addresses or user-agent
strings. The accepted `ref` value is validated and discarded; only daily event,
page and language counters are persisted in KV.

## Data model

KV stores counters with a 400-day TTL:

- `d:<date>:t:<type>` — daily total by event type;
- `d:<date>:l:<lang>:t:<type>` — daily language total;
- `d:<date>:p:<encoded-page>:t:<type>` — daily page total.

Supported types are `whatsapp`, `tel`, `form_submit` and `form_view`. Dates use
the `Europe/Lisbon` calendar day. No raw events are retained. Same-isolate
writes are serialized; Cloudflare KV remains eventually consistent across edge
locations, which is appropriate for this low-volume operational counter.
The event route also applies a deliberately anonymous per-isolate limit of 120
requests per minute. It uses no client identifier, IP address or fingerprint.

## One-time deployment

Deployment changes Cloudflare account state and requires owner approval. From
the repository root:

```bash
cd worker/leads
npx wrangler login
npx wrangler kv namespace create LEAD_COUNTS
```

Copy the returned namespace ID into `wrangler.toml`, then set the stats token:

```bash
npx wrangler secret put STATS_TOKEN
npx wrangler deploy
```

The owner keeps the same token locally in `.secrets/leads.env`:

```dotenv
ICM_LEADS_STATS_URL=https://icm-leads.vg-ab6.workers.dev/stats
ICM_LEADS_STATS_TOKEN=<same-secret-value>
```

`.secrets/` is gitignored. Never put the token in tracked files or command
output.

## API checks

The public event endpoint accepts only the production apex and `www` origins:

```bash
curl -i -X POST https://icm-leads.vg-ab6.workers.dev/event \
  -H 'Origin: https://ironcustommotors.com' \
  -H 'Content-Type: text/plain;charset=UTF-8' \
  --data '{"type":"whatsapp","page":"/contact/","lang":"en","ref":"direct"}'
```

Stats are private and are normally read with `tools/leads_report.py`. A direct
request without `token` must return `401`; an event request from any other
origin must return `403` without an `Access-Control-Allow-Origin` header.

## Local verification

```bash
node --test worker.test.mjs
```
