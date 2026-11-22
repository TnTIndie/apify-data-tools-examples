"""Yahoo Finance Historical Prices Scraper ($0.5/1K rows)

Yahoo Finance historical prices scraper for stock prices: date, open, high, low, close, adjusted close, volume, dividends and splits. Takes symbols of stocks, ETFs, indices, crypto or currency pairs, a date range and an interval. Use it to build OHLC price history for backtests or charts.

Apify page: https://apify.com/tamnt67/yahoo-finance-history-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "symbols": [
        "AAPL",
        "MSFT",
        "BTC-USD",
        "^GSPC",
        "EURUSD=X"
    ],
    "range": "1y",
    "interval": "1d"
}

run = client.actor("tamnt67/yahoo-finance-history-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
