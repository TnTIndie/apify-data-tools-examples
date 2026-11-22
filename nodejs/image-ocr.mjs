// Image OCR: Image to Text, 100+ Languages ($3/1K)
// Image OCR text extraction with Tesseract: recognized text, confidence score, line, word and character counts. Takes image URLs (screenshots, scans, receipts, labels, photos of text) and OCR languages, 100+ supported. Use it to turn images into text without an external OCR API.
// Apify page: https://apify.com/tamnt67/image-ocr
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "imageUrls": [
        {
            "url": "https://tesseract.projectnaptha.com/img/eng_bw.png"
        },
        {
            "url": "https://raw.githubusercontent.com/naptha/tesseract.js/master/tests/assets/images/testocr.png"
        }
    ],
    "languages": "eng"
};

const run = await client.actor('tamnt67/image-ocr').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
