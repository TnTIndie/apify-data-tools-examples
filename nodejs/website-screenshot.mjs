// Website Screenshot: Full Page, PNG/JPEG, Bulk ($2.5/1K)
// Website screenshot capture with real Chrome: screenshot download link, page title, final URL, HTTP status, image size and format. Takes a list of URLs, full page or visible area, PNG or JPEG, any viewport width (desktop or mobile). Use it to archive web pages or check how sites render.
// Apify page: https://apify.com/tamnt67/website-screenshot
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "urls": [
        "https://apify.com",
        "https://www.wikipedia.org"
    ],
    "fullPage": true,
    "format": "jpeg"
};

const run = await client.actor('tamnt67/website-screenshot').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
