// Leboncoin Listings Scraper: France Classified Ads, Prices
// Leboncoin listings scraper for leboncoin.fr classified ads: title, price, category, city, region, coordinates, seller type (pro or private), attributes and publish date. Takes keywords or any Leboncoin search URL with filters (France). Use it to track prices of cars, property or goods in France.
// Apify page: https://apify.com/tamnt67/leboncoin-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "keywords": [
        "vélo électrique"
    ],
    "sortBy": "time",
    "maxItemsPerQuery": 50
};

const run = await client.actor('tamnt67/leboncoin-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
