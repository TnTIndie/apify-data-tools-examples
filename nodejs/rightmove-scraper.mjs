// Rightmove Property Listings Scraper: UK Sale & Rent ($1/1K)
// Rightmove property listings scraper: price, bedrooms, bathrooms, property type, size, tenure, address, coordinates, first listed date and estate agent. Takes Rightmove search URLs for UK property for sale or to rent. Use it to track UK house prices and rentals.
// Apify page: https://apify.com/tamnt67/rightmove-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "startUrls": [
        {
            "url": "https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E904"
        }
    ],
    "maxPagesPerSearch": 5,
    "maxItems": 120
};

const run = await client.actor('tamnt67/rightmove-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
