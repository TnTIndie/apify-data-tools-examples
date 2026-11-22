"""YouTube Comments Scraper (comments, replies, likes, authors)

YouTube comments scraper: comment text, author, likes, reply count, published time, pinned and hearted flags, plus YouTube replies with their parent comment. Takes video URLs or IDs, top or newest first, no API key. Use it for sentiment analysis of a video's audience.

Apify page: https://apify.com/tamnt67/youtube-comments-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "videoUrls": [
        "https://youtu.be/i-4o4QLugK4"
    ],
    "maxCommentsPerVideo": 80,
    "sortBy": "newest",
    "includeReplies": True,
    "maxRepliesPerComment": 10
}

run = client.actor("tamnt67/youtube-comments-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
