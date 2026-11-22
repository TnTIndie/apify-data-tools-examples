"""Hacker News Stories & Comments Scraper ($1/1K)

Hacker News stories and comments scraper: title, URL, domain, points, comment count, author, date and text, also for Show HN, Ask HN, jobs and the front page. Takes keywords with filters for points, comments, dates, author or domain. Use it to track mentions of a product on HN.

Apify page: https://apify.com/tamnt67/hacker-news-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "queries": [
        "AI agent"
    ],
    "itemType": "story",
    "sortBy": "date",
    "maxItemsPerQuery": 40
}

run = client.actor("tamnt67/hacker-news-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
