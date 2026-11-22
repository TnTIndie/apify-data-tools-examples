// Polymarket & Kalshi Odds Scraper ($1/1K markets)
// Polymarket and Kalshi odds scraper for prediction markets: question, outcome, implied probability, bid, ask, last price, 24h change, volume, liquidity and end date. Takes keywords, the sources to read and a minimum volume. Use it to track prediction market odds on elections, sports or economics.
// Apify page: https://apify.com/tamnt67/prediction-markets-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "sources": [
        "polymarket",
        "kalshi"
    ],
    "maxMarketsPerSource": 60,
    "includeRules": false
};

const run = await client.actor('tamnt67/prediction-markets-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
