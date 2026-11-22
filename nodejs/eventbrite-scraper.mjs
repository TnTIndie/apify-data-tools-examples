// Eventbrite Events Scraper: Venues, Dates, Prices ($2/1K)
// Eventbrite events scraper: name, summary, start and end time, venue, address, coordinates, category, online flag and ticket link; details add price, free flag and organizer. Takes keywords and locations or Eventbrite search URLs. Use it to build local event calendars.
// Apify page: https://apify.com/tamnt67/eventbrite-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "searchUrls": [
        "https://www.eventbrite.com/d/ny--new-york/tech-events/"
    ],
    "maxEventsPerSearch": 30,
    "includeDetails": true
};

const run = await client.actor('tamnt67/eventbrite-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
