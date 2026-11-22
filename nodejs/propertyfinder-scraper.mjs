// Property Finder Listings: UAE, Saudi, Qatar, Egypt ($0.8/1K)
// Property Finder listings scraper: price, rent period, property type, bedrooms, bathrooms, size, location, coordinates, amenities, agency and photos. Takes search URLs or a country, purpose and type for the UAE, Saudi Arabia, Qatar, Bahrain and Egypt. Use it to track Dubai property prices.
// Apify page: https://apify.com/tamnt67/propertyfinder-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "startUrls": [
        {
            "url": "https://www.propertyfinder.ae/en/search?c=1&l=1&ob=mr"
        }
    ],
    "maxItems": 100
};

const run = await client.actor('tamnt67/propertyfinder-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
