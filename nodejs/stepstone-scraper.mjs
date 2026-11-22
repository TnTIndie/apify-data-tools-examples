// StepStone Jobs Scraper (Germany, Austria, Belgium, NL)
// StepStone jobs scraper: title, company, location, posting date, salary range, benefits, skills and job URL. Takes keywords and city or StepStone search URLs for Germany, Austria, Belgium and the Netherlands. Use it to track German job listings and salaries.
// Apify page: https://apify.com/tamnt67/stepstone-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "keywords": [
        "python"
    ],
    "location": "Berlin",
    "sortBy": "date",
    "maxItemsPerSearch": 40
};

const run = await client.actor('tamnt67/stepstone-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
