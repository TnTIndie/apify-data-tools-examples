// ATS Jobs Scraper (Greenhouse, Lever, Ashby, Recruitee)
// Greenhouse jobs, Lever jobs, Ashby jobs and Recruitee jobs scraper: title, department, location, remote flag, employment type, salary where published, posting date and description. Takes company job board names, with title, location and date filters. Use it to track hiring at target companies.
// Apify page: https://apify.com/tamnt67/ats-jobs-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "companies": [
        "https://boards.greenhouse.io/stripe",
        "https://jobs.lever.co/spotify",
        "https://jobs.ashbyhq.com/openai"
    ],
    "maxJobsPerCompany": 40
};

const run = await client.actor('tamnt67/ats-jobs-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
