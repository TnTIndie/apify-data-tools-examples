"""Google News Articles Scraper: Keywords, Topics, Countries

Google News articles scraper: headline, publisher, publisher website, publish date, link and related coverage. Takes keywords or topics in any language and country, with date ranges to go past the 100-article limit. Use it to monitor news about a brand, company or topic.

Apify page: https://apify.com/tamnt67/google-news-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "queries": [
        "artificial intelligence"
    ],
    "timeRange": "7d",
    "maxItemsPerQuery": 40
}

run = client.actor("tamnt67/google-news-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
