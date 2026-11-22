// HTTP Request Tool: GET/POST via Proxy ($1/1K requests)
// HTTP request tool for APIs: send GET, POST, PUT, PATCH, DELETE or HEAD and get status, headers, body, parsed JSON, redirects and timing. Takes URLs or a batch of requests, each with its own method, headers, params, body and label, plus proxy country and callback URL. Use it to call APIs.
// Apify page: https://apify.com/tamnt67/http-request-tool
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "urls": [
        {
            "url": "https://api.github.com/repos/apify/crawlee"
        },
        {
            "url": "https://example.com/"
        },
        {
            "url": "https://www.python.org/"
        },
        {
            "url": "https://nodejs.org/dist/index.json"
        },
        {
            "url": "https://registry.npmjs.org/apify/latest"
        },
        {
            "url": "https://httpbin.org/status/404"
        }
    ],
    "maxBodyChars": 5000
};

const run = await client.actor('tamnt67/http-request-tool').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
