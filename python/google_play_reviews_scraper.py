"""Google Play Reviews Scraper (ratings, text, dev replies)

Google Play reviews scraper: star rating, review text, author, date, thumbs up, app version and developer reply. Takes package names or Play Store URLs, any country and language, with sort order and star filter. Use it to analyze Android app reviews and user feedback.

Apify page: https://apify.com/tamnt67/google-play-reviews-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "appIds": [
        "com.spotify.music"
    ],
    "maxReviewsPerApp": 250,
    "sortBy": "newest",
    "country": "us",
    "language": "en"
}

run = client.actor("tamnt67/google-play-reviews-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
