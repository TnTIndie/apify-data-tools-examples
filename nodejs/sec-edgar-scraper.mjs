// SEC EDGAR Filings & Financials Scraper ($3/1K)
// SEC EDGAR filings scraper: 10-K, 10-Q, 8-K filings, XBRL financials and ratios, Form 4 insider trades, 13F holdings, 13D/13G stakes, Form D raises, full-text search hits. Takes tickers, CIKs, company names or a search phrase. Use it to track filings, insiders and fundamentals.
// Apify page: https://apify.com/tamnt67/sec-edgar-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "mode": "insiders",
    "tickers": [
        "TSLA",
        "NVDA"
    ]
};

const run = await client.actor('tamnt67/sec-edgar-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
