// AliExpress Products Scraper: Prices, Orders, Ratings
// AliExpress products scraper: title, sale price, discount, star rating, number sold, images, ad flag and product URL. Takes keywords or AliExpress search URLs with your filters. Use it to find trending products and prices for dropshipping research.
// Apify page: https://apify.com/tamnt67/aliexpress-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "keywords": [
        "wireless earbuds"
    ],
    "sortBy": "orders",
    "maxItemsPerQuery": 80
};

const run = await client.actor('tamnt67/aliexpress-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
