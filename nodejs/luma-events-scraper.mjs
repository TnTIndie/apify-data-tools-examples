// Luma Events Scraper: Tech Meetups by City ($2/1K)
// Luma events scraper for lu.ma: name, URL, start and end time, city, venue, free or paid, ticket price, sold out, spots left, guest count and organizer. Takes cities and an optional keyword. Use it to find tech meetups, AI and startup events in a city.
// Apify page: https://apify.com/tamnt67/luma-events-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "cities": [
        "sf"
    ],
    "keyword": "ai",
    "maxEventsPerCity": 100
};

const run = await client.actor('tamnt67/luma-events-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
