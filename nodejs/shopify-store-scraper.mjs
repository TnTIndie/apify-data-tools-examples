// Shopify Store Scraper: Theme, Apps & Tech Stack ($1.5/1K)
// Shopify store scraper: theme, 45+ installed apps, tracking IDs, payment options, socials, location and product count, plus products with variants, collections and catalog stats. Takes store domains or product URLs. Use it to research competitors and qualify Shopify leads by app or theme.
// Apify page: https://apify.com/tamnt67/shopify-store-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "mode": "store_detect",
    "domains": [
        "www.taylorstitch.com",
        "colourpop.com",
        "allbirds.com"
    ]
};

const run = await client.actor('tamnt67/shopify-store-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
