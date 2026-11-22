// App Store Reviews Scraper (iOS ratings, text, any country)
// App Store reviews scraper for iOS apps: star rating, title, text, author, app version, helpful votes and date, plus app rating and developer. Takes app IDs or Apple App Store URLs and a list of countries. Use it to track iPhone app ratings and user feedback.
// Apify page: https://apify.com/tamnt67/app-store-reviews-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "appIds": [
        "324684580"
    ],
    "countries": [
        "us",
        "gb"
    ],
    "sortBy": "mostrecent",
    "maxReviewsPerApp": 120
};

const run = await client.actor('tamnt67/app-store-reviews-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
