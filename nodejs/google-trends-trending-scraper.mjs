// Google Trends Trending Now Scraper ($2/1K trends)
// Google Trends trending searches scraper: keyword, rank, approximate search volume, start time and linked news stories. Takes a list of countries and reads the Google Trends Trending Now feed. Use it to spot daily trending topics and keywords in any country.
// Apify page: https://apify.com/tamnt67/google-trends-trending-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "countries": [
        "US",
        "GB",
        "IN"
    ],
    "maxItemsPerCountry": 100
};

const run = await client.actor('tamnt67/google-trends-trending-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
