// Yahoo Finance Historical Prices Scraper ($0.5/1K rows)
// Yahoo Finance historical prices scraper for stock prices: date, open, high, low, close, adjusted close, volume, dividends and splits. Takes symbols of stocks, ETFs, indices, crypto or currency pairs, a date range and an interval. Use it to build OHLC price history for backtests or charts.
// Apify page: https://apify.com/tamnt67/yahoo-finance-history-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "symbols": [
        "AAPL",
        "MSFT",
        "BTC-USD",
        "^GSPC",
        "EURUSD=X"
    ],
    "range": "1y",
    "interval": "1d"
};

const run = await client.actor('tamnt67/yahoo-finance-history-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
