// App Store ASO Keyword Scraper: Difficulty & Ranks ($2/1K)
// App Store ASO keyword scraper: difficulty and opportunity scores, top 10 ranked apps, related keywords and your app's rank, plus search results, app details, reviews and top charts. Takes keywords, app IDs or developer IDs and a country. Use it to pick ASO keywords and track app ranks.
// Apify page: https://apify.com/tamnt67/app-store-aso-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "mode": "aso_keyword",
    "keywords": [
        "habit tracker",
        "budget planner",
        "meditation"
    ],
    "country": "us"
};

const run = await client.actor('tamnt67/app-store-aso-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
