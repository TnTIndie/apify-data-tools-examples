// SmartRecruiters Jobs Scraper ($1/1K jobs)
// SmartRecruiters jobs scraper: title, department, function, employment type, experience level, location, remote flag, posting date and full description. Takes SmartRecruiters company IDs (e.g. Bosch), with keyword and country filters. Use it to track roles at companies that hire on SmartRecruiters.
// Apify page: https://apify.com/tamnt67/smartrecruiters-jobs-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "companies": [
        "BoschGroup",
        "https://jobs.smartrecruiters.com/Visa"
    ],
    "maxJobsPerCompany": 40,
    "includeDescription": true
};

const run = await client.actor('tamnt67/smartrecruiters-jobs-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
