// Remote Jobs Scraper: 5 job boards in one ($1.5/1K jobs)
// Remote jobs scraper for Remote OK, Jobicy, Himalayas, We Work Remotely and Arbeitnow: title, company, location, employment type, category, tags, salary where published, posting date and description. Takes keywords, sources and a posted-within limit. Use it to build a remote job feed.
// Apify page: https://apify.com/tamnt67/remote-jobs-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "sources": [
        "remoteok",
        "jobicy",
        "himalayas",
        "weworkremotely",
        "arbeitnow"
    ],
    "maxJobsPerSource": 30,
    "includeDescription": true
};

const run = await client.actor('tamnt67/remote-jobs-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
