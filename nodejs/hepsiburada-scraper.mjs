// Hepsiburada Products Scraper: Prices, Ratings, Sellers
// Hepsiburada products scraper: name, brand, price, original price, discount rate, rating, review count, merchant and stock. Takes keywords or Hepsiburada search and category URLs (Turkey). Use it to monitor Turkish e-commerce prices and sellers.
// Apify page: https://apify.com/tamnt67/hepsiburada-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "keywords": [
        "bluetooth kulaklık"
    ],
    "sortBy": "coklusatis",
    "maxItemsPerQuery": 50
};

const run = await client.actor('tamnt67/hepsiburada-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
