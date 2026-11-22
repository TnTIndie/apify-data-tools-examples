// Zillow Listings Scraper: Homes for Sale and Rent
// Zillow listings scraper for homes and properties: price, beds, baths, living area, address, home type, listing status, days on Zillow and Zestimate. Takes any zillow.com search URL with your filters (for sale, for rent, sold; city, ZIP or map). Use it to analyze US home prices and rentals.
// Apify page: https://apify.com/tamnt67/zillow-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "startUrls": [
        {
            "url": "https://www.zillow.com/austin-tx/rentals/"
        }
    ],
    "maxItemsPerUrl": 60
};

const run = await client.actor('tamnt67/zillow-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
