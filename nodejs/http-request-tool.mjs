// HTTP Request Tool: GET/POST via Proxy ($1/1K requests)
// HTTP request tool: status code, headers, body, parsed JSON, final URL, redirects, size and response time for each request. Takes URLs with GET, POST, PUT, PATCH, DELETE or HEAD, custom headers, body and optional proxy country. Use it to call an API or check URLs from a workflow.
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
