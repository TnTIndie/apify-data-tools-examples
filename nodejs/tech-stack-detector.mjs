// Website Tech Stack Detector: CMS, Analytics ($3/1K)
// Website tech stack detector for website technologies: CMS, ecommerce platform, JavaScript framework, analytics, ad pixels, live chat, payments, CDN, hosting and server, with evidence. Takes a list of domains or URLs. Use it to find sites built with Shopify or WordPress for lead lists.
// Apify page: https://apify.com/tamnt67/tech-stack-detector
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "urls": [
        "allbirds.com",
        "gymshark.com",
        "shopify.com",
        "squarespace.com",
        "wix.com"
    ],
    "maxConcurrency": 5
};

const run = await client.actor('tamnt67/tech-stack-detector').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
