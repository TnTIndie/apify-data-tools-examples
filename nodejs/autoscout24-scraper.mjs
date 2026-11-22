// AutoScout24 Car Listings Scraper
// AutoScout24 car listings scraper: make, model, price, mileage, first registration, fuel, gearbox, power, seller type and location. Takes any AutoScout24 search URL with your filters (.com, .de, .it, .fr, .es, .nl, .be, .at). Use it to compare used car prices across Europe.
// Apify page: https://apify.com/tamnt67/autoscout24-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "startUrls": [
        {
            "url": "https://www.autoscout24.com/lst/bmw/3-series?atype=C&cy=D&sort=standard&desc=0"
        }
    ],
    "sortBy": "url",
    "maxItemsPerUrl": 50
};

const run = await client.actor('tamnt67/autoscout24-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
