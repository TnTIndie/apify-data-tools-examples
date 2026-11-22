"""Image OCR: Image to Text, 100+ Languages ($3/1K)

Image OCR text extraction with Tesseract: recognized text, confidence score, line, word and character counts. Takes image URLs (screenshots, scans, receipts, labels, photos of text) and OCR languages, 100+ supported. Use it to turn images into text without an external OCR API.

Apify page: https://apify.com/tamnt67/image-ocr
Setup: pip install apify-client, then set the APIFY_TOKEN environment variable
(free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "imageUrls": [
        {
            "url": "https://tesseract.projectnaptha.com/img/eng_bw.png"
        },
        {
            "url": "https://raw.githubusercontent.com/naptha/tesseract.js/master/tests/assets/images/testocr.png"
        }
    ],
    "languages": "eng"
}

run = client.actor("tamnt67/image-ocr").call(run_input=run_input)
# apify-client 1.x returns a dict, 2.x returns a Run object.
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
items = list(client.dataset(dataset_id).iterate_items())
print(f"{len(items)} records")
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
