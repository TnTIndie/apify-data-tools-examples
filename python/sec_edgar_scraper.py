"""SEC EDGAR Filings & Financials Scraper ($3/1K)

SEC EDGAR filings scraper: 10-K, 10-Q, 8-K filings, XBRL financials and ratios, Form 4 insider trades, 13F holdings, 13D/13G stakes, Form D raises, full-text search hits. Takes tickers, CIKs, company names or a search phrase. Use it to track filings, insiders and fundamentals.

Apify page: https://apify.com/tamnt67/sec-edgar-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "mode": "insiders",
    "tickers": [
        "TSLA",
        "NVDA"
    ]
}

run = client.actor("tamnt67/sec-edgar-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
