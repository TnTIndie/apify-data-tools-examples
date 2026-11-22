// Shine Jobs Scraper: Shine.com India ($1.5/1K jobs)
// Shine jobs scraper for Shine.com in India: title, company, location, experience, salary in INR, skills, employment type, posting date and, with Include details, the full description. Takes keywords and a city or Shine.com search URLs. Use it to track Indian job listings and salaries.
// Apify page: https://apify.com/tamnt67/shine-jobs-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "queries": [
        "python developer"
    ],
    "location": "Bangalore",
    "maxPagesPerSearch": 5,
    "maxItems": 100,
    "includeDetails": true
};

const run = await client.actor('tamnt67/shine-jobs-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
