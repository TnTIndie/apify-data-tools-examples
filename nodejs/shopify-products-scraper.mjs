// Shopify Products Scraper (prices, variants, stock)
// Shopify products scraper: title, vendor, product type, tags, price, compare-at price, variants with SKUs, availability and images. Takes Shopify store domains or collection URLs. Use it to monitor a competitor store's catalog, prices and discounts.
// Apify page: https://apify.com/tamnt67/shopify-products-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "stores": [
        "https://www.allbirds.com",
        "brooklinen.com"
    ],
    "maxProductsPerStore": 40
};

const run = await client.actor('tamnt67/shopify-products-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
