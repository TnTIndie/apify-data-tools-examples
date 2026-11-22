// Built In Jobs Scraper: Tech & Startup Jobs ($1/1K)
// Built In jobs scraper for builtin.com tech and startup jobs: title, company, location, remote or hybrid, salary range, seniority, industry, summary and top skills. Takes keywords, a remote-only switch or Built In search URLs. Use it to track startup hiring and tech salaries.
// Apify page: https://apify.com/tamnt67/builtin-jobs-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "queries": [
        "product manager"
    ],
    "remoteOnly": true,
    "maxPagesPerSearch": 3,
    "maxItems": 120
};

const run = await client.actor('tamnt67/builtin-jobs-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
