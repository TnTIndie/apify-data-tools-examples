// Redfin Listings Scraper: US Homes for Sale ($1/1K homes)
// Redfin listings scraper for homes for sale: price, beds, baths, square feet, price per sq ft, year built, address, coordinates, days on market and last sold date. Takes Redfin city, county or neighborhood URLs (US), with price and bedroom filters. Use it to analyze US real estate listings.
// Apify page: https://apify.com/tamnt67/redfin-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "startUrls": [
        {
            "url": "https://www.redfin.com/city/30818/TX/Austin"
        }
    ],
    "maxItems": 200
};

const run = await client.actor('tamnt67/redfin-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
