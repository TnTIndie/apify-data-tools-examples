// RSS Feed Reader: RSS, Atom & JSON Feed to JSON ($1/1K)
// RSS feed reader for RSS, Atom and JSON Feed items: title, link, author, publish date, categories, summary, full content and attachments. Takes feed URLs, or website URLs and finds their feed. Use it to collect news articles or blog posts into a dataset.
// Apify page: https://apify.com/tamnt67/rss-feed-reader
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "feedUrls": [
        "https://hnrss.org/frontpage",
        "https://feeds.bbci.co.uk/news/rss.xml",
        "https://github.blog/feed/"
    ],
    "maxItemsPerFeed": 15,
    "includeContent": true
};

const run = await client.actor('tamnt67/rss-feed-reader').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
