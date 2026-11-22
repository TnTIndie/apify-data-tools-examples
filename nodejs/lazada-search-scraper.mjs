// Lazada & Daraz Products Scraper: Vietnam, Thailand, S. Asia
// Lazada products and Daraz products scraper: name, price, discount, rating, review count, sold count, seller and brand. Takes keywords or search, category and brand URLs for Lazada Vietnam and Thailand and Daraz Pakistan, Bangladesh, Sri Lanka, Nepal and Myanmar. Use it to track prices and sellers.
// Apify page: https://apify.com/tamnt67/lazada-search-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "keywords": [
        "air fryer"
    ],
    "country": "th",
    "sortBy": "popularity",
    "maxItemsPerQuery": 80
};

const run = await client.actor('tamnt67/lazada-search-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
