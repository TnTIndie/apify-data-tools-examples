// Subito.it Ads Scraper: Italy Classified Listings ($2/1K)
// Subito ads scraper for Subito.it classified listings: title, description, price, category, condition, shipping, date, region, province, town, seller type and photos. Takes search terms or Subito.it search URLs (Italy). Use it to track prices of cars, property or goods in Italy.
// Apify page: https://apify.com/tamnt67/subito-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "queries": [
        "iphone 15"
    ],
    "maxItems": 200
};

const run = await client.actor('tamnt67/subito-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
