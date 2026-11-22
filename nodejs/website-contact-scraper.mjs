// Website Contact Scraper (emails, phones, social links)
// Website contact scraper: emails, phone numbers and social links (LinkedIn, Facebook, Instagram, X, YouTube, TikTok) for each site. Takes a list of domains or URLs and checks the homepage plus contact, about and imprint pages. Use it to build lead lists with email addresses from company websites.
// Apify page: https://apify.com/tamnt67/website-contact-scraper
// Setup: npm install apify-client, then set the APIFY_TOKEN environment variable
// (free Apify account: https://console.apify.com/sign-up, token under Settings > API & Integrations).
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
    "websites": [
        "apify.com",
        "https://crawlee.dev"
    ],
    "maxPagesPerSite": 5
};

const run = await client.actor('tamnt67/website-contact-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} records`);
for (const item of items.slice(0, 5)) console.log(JSON.stringify(item).slice(0, 500));
