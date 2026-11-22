// Gupy Jobs Scraper: Brazil Job Openings ($1.5/1K jobs)
// Gupy jobs scraper for Brazil job openings: title, company, department, city, state, workplace type (remote, hybrid, on-site), job type, publish date and full description. Takes keywords for the Gupy job portal or company career pages. Use it to track Brazilian hiring.
// Apify page: https://apify.com/tamnt67/gupy-jobs-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "searchTerms": [
        "desenvolvedor",
        "engenheiro de dados"
    ],
    "workplaceType": "remote",
    "maxResults": 200,
    "includeDetails": true
};

const run = await client.actor('tamnt67/gupy-jobs-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
