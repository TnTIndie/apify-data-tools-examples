// Flipkart Products Scraper: Prices, Discounts, Ratings
// Flipkart products scraper: title, brand, price, MRP, discount, rating, rating and review counts, stock and Flipkart Assured flag. Takes keywords or Flipkart search and category URLs (India). Use it to track Flipkart prices and discounts or compare products in a category.
// Apify page: https://apify.com/tamnt67/flipkart-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "keywords": [
        "wireless earphones"
    ],
    "sortBy": "popularity",
    "maxItemsPerQuery": 60
};

const run = await client.actor('tamnt67/flipkart-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
