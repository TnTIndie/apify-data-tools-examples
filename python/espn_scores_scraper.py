"""ESPN Scores Scraper: NBA, NFL, Soccer, Tennis ($2/1K)

ESPN scores scraper for live scores, results and schedules: teams, scores, period scores, status, venue, broadcasts and betting lines. Takes leagues (NBA, NFL, MLB, NHL, Premier League, Champions League, ATP, WTA and more) and dates. Use it to feed sports scores into apps or models.

Apify page: https://apify.com/tamnt67/espn-scores-scraper
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "leagues": [
        "nba",
        "soccer/eng.1"
    ],
    "dates": "yesterday"
}

run = client.actor("tamnt67/espn-scores-scraper").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
