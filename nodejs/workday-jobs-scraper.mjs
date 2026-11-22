// Workday Jobs Scraper ($1/1K jobs)
// Workday jobs scraper for myworkdayjobs.com career sites: title, location, job ID, posting date, time type, remote type and full description. Takes the Workday career site URLs of any company. Use it to track open roles at large employers.
// Apify page: https://apify.com/tamnt67/workday-jobs-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "careerSites": [
        "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite",
        "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site"
    ],
    "maxJobsPerSite": 40,
    "includeDetails": true
};

const run = await client.actor('tamnt67/workday-jobs-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
