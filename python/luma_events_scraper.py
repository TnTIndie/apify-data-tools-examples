"""Luma Events Scraper: Tech Meetups by City ($2/1K)

Luma events scraper for lu.ma: name, URL, start and end time, city, venue, free or paid, ticket price, sold out, spots left, guest count and organizer. Takes cities and an optional keyword. Use it to find tech meetups, AI and startup events in a city.

Apify page: https://apify.com/tamnt67/luma-events-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "cities": [
        "sf"
    ],
    "keyword": "ai",
    "maxEventsPerCity": 100
}

run = client.actor("tamnt67/luma-events-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
