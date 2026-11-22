"""Eventbrite Events Scraper: Venues, Dates, Prices ($2/1K)

Eventbrite events scraper: name, summary, start and end time, venue, address, coordinates, category, online flag and ticket link; details add price, free flag and organizer. Takes keywords and locations or Eventbrite search URLs. Use it to build local event calendars.

Apify page: https://apify.com/tamnt67/eventbrite-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "searchUrls": [
        "https://www.eventbrite.com/d/ny--new-york/tech-events/"
    ],
    "maxEventsPerSearch": 30,
    "includeDetails": True
}

run = client.actor("tamnt67/eventbrite-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
