// Rakuten Products Scraper: Japan Prices, Points, Shops
// Rakuten products scraper for Rakuten Ichiba Japan: name, price, Rakuten points, review score and count, shop, shipping fee, genre and URL. Takes keywords in Japanese or English, or rakuten.co.jp search and genre URLs. Use it to research prices and shops on Rakuten Japan.
// Apify page: https://apify.com/tamnt67/rakuten-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "keywords": [
        "ワイヤレスイヤホン"
    ],
    "sortBy": "reviews",
    "maxItemsPerQuery": 60
};

const run = await client.actor('tamnt67/rakuten-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
