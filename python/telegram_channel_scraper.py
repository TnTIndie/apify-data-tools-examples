"""Telegram Channel Scraper (posts, views, reactions, media)

Telegram channel posts scraper: text, date, views, reactions, photos, videos, links and forwards, plus channel title and subscriber count. Takes public channel usernames or t.me links, no login or bot token. Use it to monitor Telegram messages from public news or community channels.

Apify page: https://apify.com/tamnt67/telegram-channel-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "channels": [
        "https://t.me/bloomberg",
        "telegram"
    ],
    "maxPostsPerChannel": 50,
    "includeChannelInfo": True
}

run = client.actor("tamnt67/telegram-channel-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
