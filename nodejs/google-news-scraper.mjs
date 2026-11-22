// Google News Articles Scraper: Keywords, Topics, Countries
// Google News articles scraper: headline, publisher, publisher website, publish date, link and related coverage. Takes keywords or topics in any language and country, with date ranges to go past the 100-article limit. Use it to monitor news about a brand, company or topic.
// Apify page: https://apify.com/tamnt67/google-news-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "queries": [
        "artificial intelligence"
    ],
    "timeRange": "7d",
    "maxItemsPerQuery": 40
};

const run = await client.actor('tamnt67/google-news-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
