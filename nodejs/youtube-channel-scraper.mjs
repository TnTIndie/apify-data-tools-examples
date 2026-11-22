// YouTube Channel Scraper (subscribers, emails, links, stats)
// YouTube channel scraper: subscribers, total views, video count, joined date, country, emails in the description, social links and latest videos. Takes YouTube channel URLs, @handles, channel IDs or keywords, no API key. Use it to find YouTube influencers and their contact emails.
// Apify page: https://apify.com/tamnt67/youtube-channel-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "channels": [
        "@mkbhd",
        "https://www.youtube.com/@veritasium"
    ],
    "recentVideosCount": 5
};

const run = await client.actor('tamnt67/youtube-channel-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
