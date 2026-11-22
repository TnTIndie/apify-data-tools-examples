// Hacker News Stories & Comments Scraper ($1/1K)
// Hacker News stories and comments scraper: title, URL, domain, points, comment count, author, date and text, also for Show HN, Ask HN, jobs and the front page. Takes keywords with filters for points, comments, dates, author or domain. Use it to track mentions of a product on HN.
// Apify page: https://apify.com/tamnt67/hacker-news-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "queries": [
        "AI agent"
    ],
    "itemType": "story",
    "sortBy": "date",
    "maxItemsPerQuery": 40
};

const run = await client.actor('tamnt67/hacker-news-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
