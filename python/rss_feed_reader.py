"""RSS Feed Reader: RSS, Atom & JSON Feed to JSON ($1/1K)

RSS feed reader for RSS, Atom and JSON Feed items: title, link, author, publish date, categories, summary, full content and attachments. Takes feed URLs, or website URLs and finds their feed. Use it to collect news articles or blog posts into a dataset.

Apify page: https://apify.com/tamnt67/rss-feed-reader
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "feedUrls": [
        "https://hnrss.org/frontpage",
        "https://feeds.bbci.co.uk/news/rss.xml",
        "https://github.blog/feed/"
    ],
    "maxItemsPerFeed": 15,
    "includeContent": True
}

run = client.actor("tamnt67/rss-feed-reader").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
