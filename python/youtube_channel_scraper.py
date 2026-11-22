"""YouTube Channel Scraper (subscribers, emails, links, stats)

YouTube channel scraper: subscribers, total views, video count, joined date, country, emails in the description, social links and latest videos. Takes YouTube channel URLs, @handles, channel IDs or keywords, no API key. Use it to find YouTube influencers and their contact emails.

Apify page: https://apify.com/tamnt67/youtube-channel-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "channels": [
        "@mkbhd",
        "https://www.youtube.com/@veritasium"
    ],
    "recentVideosCount": 5
}

run = client.actor("tamnt67/youtube-channel-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
