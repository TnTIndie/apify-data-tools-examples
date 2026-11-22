// ESPN Scores Scraper: NBA, NFL, Soccer, Tennis ($2/1K)
// ESPN scores scraper for live scores, results and schedules: teams, scores, period scores, status, venue, broadcasts and betting lines. Takes leagues (NBA, NFL, MLB, NHL, Premier League, Champions League, ATP, WTA and more) and dates. Use it to feed sports scores into apps or models.
// Apify page: https://apify.com/tamnt67/espn-scores-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "leagues": [
        "nba",
        "soccer/eng.1"
    ],
    "dates": "yesterday"
};

const run = await client.actor('tamnt67/espn-scores-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
