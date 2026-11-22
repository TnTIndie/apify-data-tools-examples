// Google Play Reviews Scraper (ratings, text, dev replies)
// Google Play reviews scraper: star rating, review text, author, date, thumbs up, app version and developer reply. Takes package names or Play Store URLs, any country and language, with sort order and star filter. Use it to analyze Android app reviews and user feedback.
// Apify page: https://apify.com/tamnt67/google-play-reviews-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "appIds": [
        "com.spotify.music"
    ],
    "maxReviewsPerApp": 250,
    "sortBy": "newest",
    "country": "us",
    "language": "en"
};

const run = await client.actor('tamnt67/google-play-reviews-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
