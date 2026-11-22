// Internshala Internships & Jobs Scraper: India ($1.5/1K)
// Internshala internships and jobs scraper: title, company, locations, work-from-home flag, stipend or salary, duration, experience, skills and posting age. Takes keywords and locations or Internshala search URLs (India). Use it to track internships and fresher jobs in India.
// Apify page: https://apify.com/tamnt67/internshala-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "type": "internships",
    "keywords": [
        "python",
        "marketing"
    ],
    "maxItemsPerSearch": 50
};

const run = await client.actor('tamnt67/internshala-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
