// Workable Jobs Scraper ($1/1K jobs)
// Workable jobs scraper: title, department, function, employment type, location, remote flag, posting date and full description. Takes Workable company account names or apply.workable.com career page URLs, with title and location filters. Use it to track open roles at companies that hire on Workable.
// Apify page: https://apify.com/tamnt67/workable-jobs-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "companies": [
        "huggingface",
        "https://apply.workable.com/blueground"
    ],
    "includeDescription": true
};

const run = await client.actor('tamnt67/workable-jobs-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
