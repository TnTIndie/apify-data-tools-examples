"""HTTP Request Tool: GET/POST via Proxy ($1/1K requests)

HTTP request tool: status code, headers, body, parsed JSON, final URL, redirects, size and response time for each request. Takes URLs with GET, POST, PUT, PATCH, DELETE or HEAD, custom headers, body and optional proxy country. Use it to call an API or check URLs from a workflow.

Apify page: https://apify.com/tamnt67/http-request-tool
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "urls": [
        {
            "url": "https://api.github.com/repos/apify/crawlee"
        },
        {
            "url": "https://example.com/"
        },
        {
            "url": "https://www.python.org/"
        },
        {
            "url": "https://nodejs.org/dist/index.json"
        },
        {
            "url": "https://registry.npmjs.org/apify/latest"
        },
        {
            "url": "https://httpbin.org/status/404"
        }
    ],
    "maxBodyChars": 5000
}

run = client.actor("tamnt67/http-request-tool").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
