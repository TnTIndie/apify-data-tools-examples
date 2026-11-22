// Netflix Prices by Country Scraper ($2/1K plans)
// Netflix prices by country: plan name, price, price text, currency, billing period, ads flag and extra member prices. Takes country codes, or all countries, and reads Netflix's official Plans and Pricing help pages. Use it to compare Netflix subscription prices worldwide.
// Apify page: https://apify.com/tamnt67/netflix-prices-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "countries": [
        "US",
        "GB",
        "IN",
        "BR",
        "DE",
        "JP",
        "VN"
    ]
};

const run = await client.actor('tamnt67/netflix-prices-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
