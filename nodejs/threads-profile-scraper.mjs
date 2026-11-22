// Threads Profile Scraper (followers, bio, latest posts)
// Threads profile scraper: username, full name, bio, follower count, verified flag, bio links and latest Threads posts with likes, replies and reposts. Takes Threads usernames or profile URLs, no login. Use it to check influencers and their followers in bulk.
// Apify page: https://apify.com/tamnt67/threads-profile-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "usernames": [
        "nasa",
        "natgeo"
    ],
    "includeLatestPosts": true
};

const run = await client.actor('tamnt67/threads-profile-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
