"""Substack Posts Scraper: Likes, Comments, Full Text ($1/1K)

Substack posts scraper: title, subtitle, author, publish date, free or paid, word count, likes, comments, restacks and full text of free posts. Takes Substack newsletter URLs, custom domains included. Use it to analyze a newsletter's archive and engagement.

Apify page: https://apify.com/tamnt67/substack-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "newsletters": [
        "lenny",
        "https://newsletter.pragmaticengineer.com"
    ],
    "maxPostsPerNewsletter": 25,
    "includeContent": True
}

run = client.actor("tamnt67/substack-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
