// YouTube Videos Scraper: Search, Channels, Playlists, Shorts
// YouTube videos scraper: title, video ID, channel, view count, publish time, duration and Shorts flag; full details add likes, comment count and description. Takes search keywords or YouTube channel, playlist and video URLs, no API key. Use it to research YouTube search results and channel videos.
// Apify page: https://apify.com/tamnt67/youtube-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "searchQueries": [
        "wireless earbuds review"
    ],
    "maxResultsPerQuery": 40,
    "videoDetails": true,
    "searchType": "video"
};

const run = await client.actor('tamnt67/youtube-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
