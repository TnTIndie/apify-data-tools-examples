// Skool Communities Scraper ($2/1K communities)
// Skool communities scraper: name, URL, description, member count, paid flag, price, rating and review count. Takes search keywords for the public Skool discovery page. Use it to research Skool groups in a niche and their pricing.
// Apify page: https://apify.com/tamnt67/skool-communities-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "searchQueries": [
        "ai automation"
    ],
    "maxResultsPerQuery": 60
};

const run = await client.actor('tamnt67/skool-communities-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
