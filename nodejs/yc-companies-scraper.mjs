// Y Combinator Companies Scraper + Jobs ($1/1K)
// Y Combinator companies scraper for YC startups: name, batch, status, industry, team size, location, website, social links and open jobs with salary ranges. Takes batches, industries, locations, keywords, status and a hiring-only switch. Use it to build startup lead lists or find YC jobs.
// Apify page: https://apify.com/tamnt67/yc-companies-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "batches": [
        "W25",
        "Summer 2025"
    ],
    "hiringOnly": true,
    "maxResults": 150,
    "includeDetails": true
};

const run = await client.actor('tamnt67/yc-companies-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
