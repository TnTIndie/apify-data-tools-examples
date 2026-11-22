// Substack Posts Scraper: Likes, Comments, Full Text ($1/1K)
// Substack posts scraper: title, subtitle, author, publish date, free or paid, word count, likes, comments, restacks and full text of free posts. Takes Substack newsletter URLs, custom domains included. Use it to analyze a newsletter's archive and engagement.
// Apify page: https://apify.com/tamnt67/substack-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "newsletters": [
        "lenny",
        "https://newsletter.pragmaticengineer.com"
    ],
    "maxPostsPerNewsletter": 25,
    "includeContent": true
};

const run = await client.actor('tamnt67/substack-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
