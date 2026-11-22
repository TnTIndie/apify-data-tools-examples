// App Store Search Scraper: ASO Keyword Ranks ($1/1K apps)
// App Store search scraper for ASO keyword rankings: rank, app name, developer, price, rating, rating count, genre, version, update date and description. Takes keywords and App Store countries. Use it to see which iOS apps rank for a keyword and track your app's rank.
// Apify page: https://apify.com/tamnt67/app-store-search-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "keywords": [
        "habit tracker",
        "meal planner",
        "vpn"
    ],
    "countries": [
        "us",
        "gb"
    ],
    "maxAppsPerKeyword": 50
};

const run = await client.actor('tamnt67/app-store-search-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
