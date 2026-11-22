// GitHub Trending Repositories Scraper ($0.8/1K)
// GitHub trending repositories scraper: rank, repository name, owner, description, language, stars, forks, stars gained in the period and contributors. Takes periods (today, this week, this month) and programming languages. Use it to spot fast-growing open source projects.
// Apify page: https://apify.com/tamnt67/github-trending-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "periods": [
        "weekly"
    ],
    "languages": [
        "all",
        "python"
    ]
};

const run = await client.actor('tamnt67/github-trending-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
