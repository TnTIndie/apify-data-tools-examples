"""YouTube Videos Scraper: Search, Channels, Playlists, Shorts

YouTube videos scraper: title, video ID, channel, view count, publish time, duration and Shorts flag; full details add likes, comment count and description. Takes search keywords or YouTube channel, playlist and video URLs, no API key. Use it to research YouTube search results and channel videos.

Apify page: https://apify.com/tamnt67/youtube-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "searchQueries": [
        "wireless earbuds review"
    ],
    "maxResultsPerQuery": 40,
    "videoDetails": True,
    "searchType": "video"
}

run = client.actor("tamnt67/youtube-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
