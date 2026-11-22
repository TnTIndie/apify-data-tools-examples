// YouTube Comments Scraper (comments, replies, likes, authors)
// YouTube comments scraper: comment text, author, likes, reply count, published time, pinned and hearted flags, plus YouTube replies with their parent comment. Takes video URLs or IDs, top or newest first, no API key. Use it for sentiment analysis of a video's audience.
// Apify page: https://apify.com/tamnt67/youtube-comments-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "videoUrls": [
        "https://youtu.be/i-4o4QLugK4"
    ],
    "maxCommentsPerVideo": 80,
    "sortBy": "newest",
    "includeReplies": true,
    "maxRepliesPerComment": 10
};

const run = await client.actor('tamnt67/youtube-comments-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
