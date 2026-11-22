"""Threads Profile Scraper (followers, bio, latest posts)

Threads profile scraper: username, full name, bio, follower count, verified flag, bio links and latest Threads posts with likes, replies and reposts. Takes Threads usernames or profile URLs, no login. Use it to check influencers and their followers in bulk.

Apify page: https://apify.com/tamnt67/threads-profile-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "usernames": [
        "nasa",
        "natgeo"
    ],
    "includeLatestPosts": True
}

run = client.actor("tamnt67/threads-profile-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
