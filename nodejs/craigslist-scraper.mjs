// Craigslist Listings Scraper: For Sale, Housing ($2/1K)
// Craigslist listings scraper: title, price, neighbourhood, URL, post ID and, where shown, bedrooms, bathrooms and coordinates. Takes Craigslist search URLs, or cities, a section (for sale, housing, jobs, services, gigs, cars) and keywords. Use it to monitor local classified ads and rentals.
// Apify page: https://apify.com/tamnt67/craigslist-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "cities": [
        "newyork"
    ],
    "category": "sss",
    "queries": [
        "bike"
    ],
    "maxItems": 200
};

const run = await client.actor('tamnt67/craigslist-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
