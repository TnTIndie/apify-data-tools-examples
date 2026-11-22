// Telegram Channel Scraper (posts, views, reactions, media)
// Telegram channel posts scraper: text, date, views, reactions, photos, videos, links and forwards, plus channel title and subscriber count. Takes public channel usernames or t.me links, no login or bot token. Use it to monitor Telegram messages from public news or community channels.
// Apify page: https://apify.com/tamnt67/telegram-channel-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "channels": [
        "https://t.me/bloomberg",
        "telegram"
    ],
    "maxPostsPerChannel": 50,
    "includeChannelInfo": true
};

const run = await client.actor('tamnt67/telegram-channel-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
