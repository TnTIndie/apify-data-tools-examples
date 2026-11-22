// Tiki Products Scraper: Tiki.vn Search, Categories, Details
// Tiki products scraper: name, price, original price, discount, rating, review count, quantity sold, seller and brand. Takes keywords, category IDs or Tiki.vn URLs (Vietnam); full details add specifications, images, variants and stock. Use it to monitor prices and top sellers on Tiki.
// Apify page: https://apify.com/tamnt67/tiki-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "keywords": [
        "tai nghe bluetooth"
    ],
    "sortBy": "top_seller",
    "maxItemsPerQuery": 45,
    "includeDetails": true
};

const run = await client.actor('tamnt67/tiki-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
