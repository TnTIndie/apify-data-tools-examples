// Google Ads Transparency Scraper (ads, advertisers, regions)
// Google Ads Transparency Center scraper for Google ads: advertiser name and ID, creative ID, ad format, first and last shown dates, image or preview link and ad URL. Takes advertiser names, AR IDs or website domains, with country, format and date filters. Use it to research competitor ads.
// Apify page: https://apify.com/tamnt67/google-ads-transparency-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "advertisers": [
        "https://adstransparency.google.com/advertiser/AR16735076323512287233"
    ],
    "regions": [
        "DE"
    ],
    "format": "any",
    "includeDetails": true,
    "maxAdsPerQuery": 45,
    "domains": []
};

const run = await client.actor('tamnt67/google-ads-transparency-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
