// Dice Jobs Scraper: US Tech Jobs ($0.9/1K jobs)
// Dice jobs scraper for US tech jobs: title, company, location, salary, employment type, posting date, Easy Apply flag and link; optional full description. Takes keywords and location or Dice.com search URLs. Use it to track tech job listings and salaries in the US.
// Apify page: https://apify.com/tamnt67/dice-jobs-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "queries": [
        "data engineer"
    ],
    "includeDescription": true,
    "maxPagesPerSearch": 2,
    "maxItems": 80
};

const run = await client.actor('tamnt67/dice-jobs-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
