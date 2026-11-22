# Web scrapers and data tools on Apify

Ready-to-run data tools for e-commerce, real estate, jobs, video, social media, news, SEO and developers.
Each one runs on [Apify](https://apify.com), so there is nothing to host: send an input, get clean JSON, CSV or Excel back.
This repo has a short description of every tool, a link to its page, and copy-paste examples in Python and Node.js.

All tools collect public data only: no login, no personal accounts.
Pricing is pay per result and is listed on each tool's page.

## Quick start

1. Create a free Apify account and copy your API token (Console > Settings > API & Integrations).
2. Python: `pip install apify-client`, then run any file in [python/](python/).
   Node.js: `npm install apify-client`, then run any file in [nodejs/](nodejs/).
3. Set the token first: `export APIFY_TOKEN=...` (macOS/Linux) or `$env:APIFY_TOKEN="..."` (PowerShell).

Every example uses an input that was tested on Apify. Change the input to your own keywords, URLs or IDs.
You can also run every tool from the Apify web console, on a schedule, through webhooks, Make, Zapier, n8n, or from an AI agent through the [Apify MCP server](https://mcp.apify.com).

## E-commerce

### [AliExpress Products Scraper: Prices, Orders, Ratings](https://apify.com/tamnt67/aliexpress-scraper)

AliExpress products scraper: title, sale price, discount, star rating, number sold, images, ad flag and product URL. Takes keywords or AliExpress search URLs with your filters. Use it to find trending products and prices for dropshipping research.

Examples: [Python](python/aliexpress_scraper.py) · [Node.js](nodejs/aliexpress-scraper.mjs) · Ready-made runs: [Find best-selling wireless earbuds on AliExpress](https://apify.com/tamnt67/aliexpress-scraper/examples/aliexpress-best-selling-earbuds)

### [AutoScout24 Car Listings Scraper](https://apify.com/tamnt67/autoscout24-scraper)

AutoScout24 car listings scraper: make, model, price, mileage, first registration, fuel, gearbox, power, seller type and location. Takes any AutoScout24 search URL with your filters (.com, .de, .it, .fr, .es, .nl, .be, .at). Use it to compare used car prices across Europe.

Examples: [Python](python/autoscout24_scraper.py) · [Node.js](nodejs/autoscout24-scraper.mjs) · Ready-made runs: [Track used BMW 3 Series prices on AutoScout24](https://apify.com/tamnt67/autoscout24-scraper/examples/autoscout24-bmw-3-series-prices) · [Used VW Golf prices in Germany on AutoScout24](https://apify.com/tamnt67/autoscout24-scraper/examples/autoscout24-used-vw-golf-prices)

### [Craigslist Listings Scraper: For Sale, Housing ($2/1K)](https://apify.com/tamnt67/craigslist-scraper)

Craigslist listings scraper: title, price, neighbourhood, URL, post ID and, where shown, bedrooms, bathrooms and coordinates. Takes Craigslist search URLs, or cities, a section (for sale, housing, jobs, services, gigs, cars) and keywords. Use it to monitor local classified ads and rentals.

Examples: [Python](python/craigslist_scraper.py) · [Node.js](nodejs/craigslist-scraper.mjs) · Ready-made runs: [Find used bikes for sale on Craigslist New York](https://apify.com/tamnt67/craigslist-scraper/examples/craigslist-used-bikes-new-york)

### [Flipkart Products Scraper: Prices, Discounts, Ratings](https://apify.com/tamnt67/flipkart-scraper)

Flipkart products scraper: title, brand, price, MRP, discount, rating, rating and review counts, stock and Flipkart Assured flag. Takes keywords or Flipkart search and category URLs (India). Use it to track Flipkart prices and discounts or compare products in a category.

Examples: [Python](python/flipkart_scraper.py) · [Node.js](nodejs/flipkart-scraper.mjs) · Ready-made runs: [Track wireless earphones prices on Flipkart India](https://apify.com/tamnt67/flipkart-scraper/examples/flipkart-earphones-price-tracker) · [Track smartwatch prices on Flipkart](https://apify.com/tamnt67/flipkart-scraper/examples/flipkart-smartwatch-prices) · [Export the headphones category on Flipkart](https://apify.com/tamnt67/flipkart-scraper/examples/flipkart-headphones-category)

### [Hepsiburada Products Scraper: Prices, Ratings, Sellers](https://apify.com/tamnt67/hepsiburada-scraper)

Hepsiburada products scraper: name, brand, price, original price, discount rate, rating, review count, merchant and stock. Takes keywords or Hepsiburada search and category URLs (Turkey). Use it to monitor Turkish e-commerce prices and sellers.

Examples: [Python](python/hepsiburada_scraper.py) · [Node.js](nodejs/hepsiburada-scraper.mjs) · Ready-made runs: [Track Bluetooth headphone prices on Hepsiburada](https://apify.com/tamnt67/hepsiburada-scraper/examples/hepsiburada-bluetooth-headphones-prices) · [Hepsiburada iPhone prices](https://apify.com/tamnt67/hepsiburada-scraper/examples/hepsiburada-iphone-prices)

### [Lazada & Daraz Products Scraper: Vietnam, Thailand, S. Asia](https://apify.com/tamnt67/lazada-search-scraper)

Lazada products and Daraz products scraper: name, price, discount, rating, review count, sold count, seller and brand. Takes keywords or search, category and brand URLs for Lazada Vietnam and Thailand and Daraz Pakistan, Bangladesh, Sri Lanka, Nepal and Myanmar. Use it to track prices and sellers.

Examples: [Python](python/lazada_search_scraper.py) · [Node.js](nodejs/lazada-search-scraper.mjs) · Ready-made runs: [Track air fryer prices on Lazada Thailand](https://apify.com/tamnt67/lazada-search-scraper/examples/lazada-thailand-air-fryer-prices) · [Track air purifier prices on Lazada Vietnam](https://apify.com/tamnt67/lazada-search-scraper/examples/lazada-vietnam-air-purifier-prices) · [Track earphone prices on Daraz Pakistan](https://apify.com/tamnt67/lazada-search-scraper/examples/daraz-pakistan-earphones-prices) · [Daraz Bangladesh smartphone prices](https://apify.com/tamnt67/lazada-search-scraper/examples/daraz-bangladesh-smartphone-prices) · [Daraz Sri Lanka laptop prices](https://apify.com/tamnt67/lazada-search-scraper/examples/daraz-sri-lanka-laptop-prices) · [Daraz Nepal skincare product prices](https://apify.com/tamnt67/lazada-search-scraper/examples/daraz-nepal-skincare-prices)

### [Leboncoin Listings Scraper: France Classified Ads, Prices](https://apify.com/tamnt67/leboncoin-scraper)

Leboncoin listings scraper for leboncoin.fr classified ads: title, price, category, city, region, coordinates, seller type (pro or private), attributes and publish date. Takes keywords or any Leboncoin search URL with filters (France). Use it to track prices of cars, property or goods in France.

Examples: [Python](python/leboncoin_scraper.py) · [Node.js](nodejs/leboncoin-scraper.mjs) · Ready-made runs: [Track used electric bike prices on Leboncoin](https://apify.com/tamnt67/leboncoin-scraper/examples/leboncoin-electric-bike-prices)

### [Netflix Prices by Country Scraper ($2/1K plans)](https://apify.com/tamnt67/netflix-prices-scraper)

Netflix prices by country: plan name, price, price text, currency, billing period, ads flag and extra member prices. Takes country codes, or all countries, and reads Netflix's official Plans and Pricing help pages. Use it to compare Netflix subscription prices worldwide.

Examples: [Python](python/netflix_prices_scraper.py) · [Node.js](nodejs/netflix-prices-scraper.mjs) · Ready-made runs: [Compare Netflix prices across countries](https://apify.com/tamnt67/netflix-prices-scraper/examples/netflix-prices-by-country) · [Netflix prices in Asian countries](https://apify.com/tamnt67/netflix-prices-scraper/examples/netflix-prices-asia) · [Netflix prices in European countries](https://apify.com/tamnt67/netflix-prices-scraper/examples/netflix-prices-europe)

### [Rakuten Products Scraper: Japan Prices, Points, Shops](https://apify.com/tamnt67/rakuten-scraper)

Rakuten products scraper for Rakuten Ichiba Japan: name, price, Rakuten points, review score and count, shop, shipping fee, genre and URL. Takes keywords in Japanese or English, or rakuten.co.jp search and genre URLs. Use it to research prices and shops on Rakuten Japan.

Examples: [Python](python/rakuten_scraper.py) · [Node.js](nodejs/rakuten-scraper.mjs) · Ready-made runs: [Find top-reviewed wireless earphones on Rakuten Japan](https://apify.com/tamnt67/rakuten-scraper/examples/rakuten-japan-top-reviewed-earphones) · [Compare coffee maker prices on Rakuten Japan](https://apify.com/tamnt67/rakuten-scraper/examples/rakuten-japan-coffee-maker-prices) · [Export a Rakuten Japan category with prices](https://apify.com/tamnt67/rakuten-scraper/examples/rakuten-japan-category-products)

### [Shopify Products Scraper (prices, variants, stock)](https://apify.com/tamnt67/shopify-products-scraper)

Shopify products scraper: title, vendor, product type, tags, price, compare-at price, variants with SKUs, availability and images. Takes Shopify store domains or collection URLs. Use it to monitor a competitor store's catalog, prices and discounts.

Examples: [Python](python/shopify_products_scraper.py) · [Node.js](nodejs/shopify-products-scraper.mjs) · Ready-made runs: [Track a competitor's Shopify catalog and prices](https://apify.com/tamnt67/shopify-products-scraper/examples/shopify-competitor-catalog-prices)

### [Subito.it Ads Scraper: Italy Classified Listings ($2/1K)](https://apify.com/tamnt67/subito-scraper)

Subito ads scraper for Subito.it classified listings: title, description, price, category, condition, shipping, date, region, province, town, seller type and photos. Takes search terms or Subito.it search URLs (Italy). Use it to track prices of cars, property or goods in Italy.

Examples: [Python](python/subito_scraper.py) · [Node.js](nodejs/subito-scraper.mjs) · Ready-made runs: [Track used iPhone prices on Subito.it](https://apify.com/tamnt67/subito-scraper/examples/subito-used-iphone-prices-italy) · [Used cars for sale in Lombardy on Subito.it](https://apify.com/tamnt67/subito-scraper/examples/subito-used-cars-lombardia)

### [Tiki Products Scraper: Tiki.vn Search, Categories, Details](https://apify.com/tamnt67/tiki-scraper)

Tiki products scraper: name, price, original price, discount, rating, review count, quantity sold, seller and brand. Takes keywords, category IDs or Tiki.vn URLs (Vietnam); full details add specifications, images, variants and stock. Use it to monitor prices and top sellers on Tiki.

Examples: [Python](python/tiki_scraper.py) · [Node.js](nodejs/tiki-scraper.mjs) · Ready-made runs: [Find best-selling Bluetooth headphones on Tiki Vietnam](https://apify.com/tamnt67/tiki-scraper/examples/tiki-vietnam-best-sellers) · [Export a Tiki.vn category with prices](https://apify.com/tamnt67/tiki-scraper/examples/tiki-vietnam-category-prices) · [Get full product details from Tiki.vn links](https://apify.com/tamnt67/tiki-scraper/examples/tiki-vietnam-product-details) · [Tiki.vn smartphone prices](https://apify.com/tamnt67/tiki-scraper/examples/tiki-vietnam-smartphone-prices) · [Tiki.vn best-selling books](https://apify.com/tamnt67/tiki-scraper/examples/tiki-vietnam-best-selling-books)

## Real estate

### [Property Finder Listings: UAE, Saudi, Qatar, Egypt ($0.8/1K)](https://apify.com/tamnt67/propertyfinder-scraper)

Property Finder listings scraper: price, rent period, property type, bedrooms, bathrooms, size, location, coordinates, amenities, agency and photos. Takes search URLs or a country, purpose and type for the UAE, Saudi Arabia, Qatar, Bahrain and Egypt. Use it to track Dubai property prices.

Examples: [Python](python/propertyfinder_scraper.py) · [Node.js](nodejs/propertyfinder-scraper.mjs)

### [Redfin Listings Scraper: US Homes for Sale ($1/1K homes)](https://apify.com/tamnt67/redfin-scraper)

Redfin listings scraper for homes for sale: price, beds, baths, square feet, price per sq ft, year built, address, coordinates, days on market and last sold date. Takes Redfin city, county or neighborhood URLs (US), with price and bedroom filters. Use it to analyze US real estate listings.

Examples: [Python](python/redfin_scraper.py) · [Node.js](nodejs/redfin-scraper.mjs) · Ready-made runs: [Find homes for sale in Austin, Texas on Redfin](https://apify.com/tamnt67/redfin-scraper/examples/redfin-austin-homes-for-sale)

### [Rightmove Property Listings Scraper: UK Sale & Rent ($1/1K)](https://apify.com/tamnt67/rightmove-scraper)

Rightmove property listings scraper: price, bedrooms, bathrooms, property type, size, tenure, address, coordinates, first listed date and estate agent. Takes Rightmove search URLs for UK property for sale or to rent. Use it to track UK house prices and rentals.

Examples: [Python](python/rightmove_scraper.py) · [Node.js](nodejs/rightmove-scraper.mjs) · Ready-made runs: [Find homes for sale in Manchester on Rightmove](https://apify.com/tamnt67/rightmove-scraper/examples/rightmove-manchester-homes-for-sale)

### [Zillow Listings Scraper: Homes for Sale and Rent](https://apify.com/tamnt67/zillow-scraper)

Zillow listings scraper for homes and properties: price, beds, baths, living area, address, home type, listing status, days on Zillow and Zestimate. Takes any zillow.com search URL with your filters (for sale, for rent, sold; city, ZIP or map). Use it to analyze US home prices and rentals.

Examples: [Python](python/zillow_scraper.py) · [Node.js](nodejs/zillow-scraper.mjs) · Ready-made runs: [Find rentals in Austin, Texas on Zillow](https://apify.com/tamnt67/zillow-scraper/examples/zillow-austin-rentals)

## Jobs

### [ATS Jobs Scraper (Greenhouse, Lever, Ashby, Recruitee)](https://apify.com/tamnt67/ats-jobs-scraper)

Greenhouse jobs, Lever jobs, Ashby jobs and Recruitee jobs scraper: title, department, location, remote flag, employment type, salary where published, posting date and description. Takes company job board names, with title, location and date filters. Use it to track hiring at target companies.

Examples: [Python](python/ats_jobs_scraper.py) · [Node.js](nodejs/ats-jobs-scraper.mjs) · Ready-made runs: [Monitor job openings at Stripe, Spotify and OpenAI](https://apify.com/tamnt67/ats-jobs-scraper/examples/tech-company-job-openings)

### [Built In Jobs Scraper: Tech & Startup Jobs ($1/1K)](https://apify.com/tamnt67/builtin-jobs-scraper)

Built In jobs scraper for builtin.com tech and startup jobs: title, company, location, remote or hybrid, salary range, seniority, industry, summary and top skills. Takes keywords, a remote-only switch or Built In search URLs. Use it to track startup hiring and tech salaries.

Examples: [Python](python/builtin_jobs_scraper.py) · [Node.js](nodejs/builtin-jobs-scraper.mjs) · Ready-made runs: [Find remote product manager jobs at startups (Built In)](https://apify.com/tamnt67/builtin-jobs-scraper/examples/builtin-remote-product-manager-jobs)

### [Dice Jobs Scraper: US Tech Jobs ($0.9/1K jobs)](https://apify.com/tamnt67/dice-jobs-scraper)

Dice jobs scraper for US tech jobs: title, company, location, salary, employment type, posting date, Easy Apply flag and link; optional full description. Takes keywords and location or Dice.com search URLs. Use it to track tech job listings and salaries in the US.

Examples: [Python](python/dice_jobs_scraper.py) · [Node.js](nodejs/dice-jobs-scraper.mjs) · Ready-made runs: [Find data engineer jobs on Dice](https://apify.com/tamnt67/dice-jobs-scraper/examples/dice-data-engineer-jobs)

### [Gupy Jobs Scraper: Brazil Job Openings ($1.5/1K jobs)](https://apify.com/tamnt67/gupy-jobs-scraper)

Gupy jobs scraper for Brazil job openings: title, company, department, city, state, workplace type (remote, hybrid, on-site), job type, publish date and full description. Takes keywords for the Gupy job portal or company career pages. Use it to track Brazilian hiring.

Examples: [Python](python/gupy_jobs_scraper.py) · [Node.js](nodejs/gupy-jobs-scraper.mjs) · Ready-made runs: [Find remote developer jobs in Brazil on Gupy](https://apify.com/tamnt67/gupy-jobs-scraper/examples/gupy-remote-developer-jobs-brazil) · [Data analyst jobs in Brazil from Gupy](https://apify.com/tamnt67/gupy-jobs-scraper/examples/gupy-data-analyst-jobs-brazil)

### [Internshala Internships & Jobs Scraper: India ($1.5/1K)](https://apify.com/tamnt67/internshala-scraper)

Internshala internships and jobs scraper: title, company, locations, work-from-home flag, stipend or salary, duration, experience, skills and posting age. Takes keywords and locations or Internshala search URLs (India). Use it to track internships and fresher jobs in India.

Examples: [Python](python/internshala_scraper.py) · [Node.js](nodejs/internshala-scraper.mjs) · Ready-made runs: [Find Python and marketing internships in India](https://apify.com/tamnt67/internshala-scraper/examples/internshala-python-internships) · [Work from home internships on Internshala](https://apify.com/tamnt67/internshala-scraper/examples/internshala-work-from-home-internships)

### [Remote Jobs Scraper: 5 job boards in one ($1.5/1K jobs)](https://apify.com/tamnt67/remote-jobs-scraper)

Remote jobs scraper for Remote OK, Jobicy, Himalayas, We Work Remotely and Arbeitnow: title, company, location, employment type, category, tags, salary where published, posting date and description. Takes keywords, sources and a posted-within limit. Use it to build a remote job feed.

Examples: [Python](python/remote_jobs_scraper.py) · [Node.js](nodejs/remote-jobs-scraper.mjs) · Ready-made runs: [Build a daily feed of remote jobs from 5 job boards](https://apify.com/tamnt67/remote-jobs-scraper/examples/remote-jobs-daily-feed)

### [Shine Jobs Scraper: Shine.com India ($1.5/1K jobs)](https://apify.com/tamnt67/shine-jobs-scraper)

Shine jobs scraper for Shine.com in India: title, company, location, experience, salary in INR, skills, employment type, posting date and, with Include details, the full description. Takes keywords and a city or Shine.com search URLs. Use it to track Indian job listings and salaries.

Examples: [Python](python/shine_jobs_scraper.py) · [Node.js](nodejs/shine-jobs-scraper.mjs) · Ready-made runs: [Find Python developer jobs in Bangalore on Shine](https://apify.com/tamnt67/shine-jobs-scraper/examples/shine-python-jobs-bangalore) · [Data analyst jobs in Mumbai from Shine.com](https://apify.com/tamnt67/shine-jobs-scraper/examples/shine-data-analyst-jobs-mumbai)

### [SmartRecruiters Jobs Scraper ($1/1K jobs)](https://apify.com/tamnt67/smartrecruiters-jobs-scraper)

SmartRecruiters jobs scraper: title, department, function, employment type, experience level, location, remote flag, posting date and full description. Takes SmartRecruiters company IDs (e.g. Bosch), with keyword and country filters. Use it to track roles at companies that hire on SmartRecruiters.

Examples: [Python](python/smartrecruiters_jobs_scraper.py) · [Node.js](nodejs/smartrecruiters-jobs-scraper.mjs) · Ready-made runs: [Export job openings from Bosch and Visa (SmartRecruiters)](https://apify.com/tamnt67/smartrecruiters-jobs-scraper/examples/bosch-visa-smartrecruiters-jobs)

### [StepStone Jobs Scraper (Germany, Austria, Belgium, NL)](https://apify.com/tamnt67/stepstone-scraper)

StepStone jobs scraper: title, company, location, posting date, salary range, benefits, skills and job URL. Takes keywords and city or StepStone search URLs for Germany, Austria, Belgium and the Netherlands. Use it to track German job listings and salaries.

Examples: [Python](python/stepstone_scraper.py) · [Node.js](nodejs/stepstone-scraper.mjs) · Ready-made runs: [Find Python developer jobs in Berlin on StepStone](https://apify.com/tamnt67/stepstone-scraper/examples/stepstone-berlin-python-jobs)

### [Workable Jobs Scraper ($1/1K jobs)](https://apify.com/tamnt67/workable-jobs-scraper)

Workable jobs scraper: title, department, function, employment type, location, remote flag, posting date and full description. Takes Workable company account names or apply.workable.com career page URLs, with title and location filters. Use it to track open roles at companies that hire on Workable.

Examples: [Python](python/workable_jobs_scraper.py) · [Node.js](nodejs/workable-jobs-scraper.mjs) · Ready-made runs: [Export startup job openings from Workable career pages](https://apify.com/tamnt67/workable-jobs-scraper/examples/startup-jobs-workable)

### [Workday Jobs Scraper ($1/1K jobs)](https://apify.com/tamnt67/workday-jobs-scraper)

Workday jobs scraper for myworkdayjobs.com career sites: title, location, job ID, posting date, time type, remote type and full description. Takes the Workday career site URLs of any company. Use it to track open roles at large employers.

Examples: [Python](python/workday_jobs_scraper.py) · [Node.js](nodejs/workday-jobs-scraper.mjs) · Ready-made runs: [Export all job openings from NVIDIA and Salesforce (Workday)](https://apify.com/tamnt67/workday-jobs-scraper/examples/nvidia-salesforce-workday-jobs)

## Video

### [YouTube Channel Scraper (subscribers, emails, links, stats)](https://apify.com/tamnt67/youtube-channel-scraper)

YouTube channel scraper: subscribers, total views, video count, joined date, country, emails in the description, social links and latest videos. Takes YouTube channel URLs, @handles, channel IDs or keywords, no API key. Use it to find YouTube influencers and their contact emails.

Examples: [Python](python/youtube_channel_scraper.py) · [Node.js](nodejs/youtube-channel-scraper.mjs) · Ready-made runs: [Compare tech YouTube channels: subscribers and links](https://apify.com/tamnt67/youtube-channel-scraper/examples/youtube-tech-channels-compare)

### [YouTube Comments Scraper (comments, replies, likes, authors)](https://apify.com/tamnt67/youtube-comments-scraper)

YouTube comments scraper: comment text, author, likes, reply count, published time, pinned and hearted flags, plus YouTube replies with their parent comment. Takes video URLs or IDs, top or newest first, no API key. Use it for sentiment analysis of a video's audience.

Examples: [Python](python/youtube_comments_scraper.py) · [Node.js](nodejs/youtube-comments-scraper.mjs) · Ready-made runs: [Export the newest comments from a YouTube video](https://apify.com/tamnt67/youtube-comments-scraper/examples/youtube-video-comments-export) · [Export YouTube comments to Excel](https://apify.com/tamnt67/youtube-comments-scraper/examples/export-youtube-comments-to-excel) · [Get the newest comments on a YouTube video](https://apify.com/tamnt67/youtube-comments-scraper/examples/youtube-newest-comments) · [YouTube comments with replies for sentiment analysis](https://apify.com/tamnt67/youtube-comments-scraper/examples/youtube-comments-replies-sentiment)

### [YouTube Videos Scraper: Search, Channels, Playlists, Shorts](https://apify.com/tamnt67/youtube-scraper)

YouTube videos scraper: title, video ID, channel, view count, publish time, duration and Shorts flag; full details add likes, comment count and description. Takes search keywords or YouTube channel, playlist and video URLs, no API key. Use it to research YouTube search results and channel videos.

Examples: [Python](python/youtube_scraper.py) · [Node.js](nodejs/youtube-scraper.mjs) · Ready-made runs: [Find YouTube review videos for a product](https://apify.com/tamnt67/youtube-scraper/examples/youtube-product-review-videos) · [Export the latest videos of a YouTube channel](https://apify.com/tamnt67/youtube-scraper/examples/youtube-channel-latest-videos) · [Export all videos of a YouTube playlist](https://apify.com/tamnt67/youtube-scraper/examples/youtube-playlist-export)

## Social media

### [Telegram Channel Scraper (posts, views, reactions, media)](https://apify.com/tamnt67/telegram-channel-scraper)

Telegram channel posts scraper: text, date, views, reactions, photos, videos, links and forwards, plus channel title and subscriber count. Takes public channel usernames or t.me links, no login or bot token. Use it to monitor Telegram messages from public news or community channels.

Examples: [Python](python/telegram_channel_scraper.py) · [Node.js](nodejs/telegram-channel-scraper.mjs) · Ready-made runs: [Export the latest posts from public Telegram news channels](https://apify.com/tamnt67/telegram-channel-scraper/examples/telegram-news-channel-posts) · [Export Telegram channel posts since a date](https://apify.com/tamnt67/telegram-channel-scraper/examples/telegram-channel-posts-since-date)

### [Threads Profile Scraper (followers, bio, latest posts)](https://apify.com/tamnt67/threads-profile-scraper)

Threads profile scraper: username, full name, bio, follower count, verified flag, bio links and latest Threads posts with likes, replies and reposts. Takes Threads usernames or profile URLs, no login. Use it to check influencers and their followers in bulk.

Examples: [Python](python/threads_profile_scraper.py) · [Node.js](nodejs/threads-profile-scraper.mjs) · Ready-made runs: [Compare brand profiles on Threads](https://apify.com/tamnt67/threads-profile-scraper/examples/threads-brand-profiles)

## News and feeds

### [Google News Articles Scraper: Keywords, Topics, Countries](https://apify.com/tamnt67/google-news-scraper)

Google News articles scraper: headline, publisher, publisher website, publish date, link and related coverage. Takes keywords or topics in any language and country, with date ranges to go past the 100-article limit. Use it to monitor news about a brand, company or topic.

Examples: [Python](python/google_news_scraper.py) · [Node.js](nodejs/google-news-scraper.mjs) · Ready-made runs: [Monitor this week's AI news on Google News](https://apify.com/tamnt67/google-news-scraper/examples/google-news-ai-weekly)

### [Hacker News Stories & Comments Scraper ($1/1K)](https://apify.com/tamnt67/hacker-news-scraper)

Hacker News stories and comments scraper: title, URL, domain, points, comment count, author, date and text, also for Show HN, Ask HN, jobs and the front page. Takes keywords with filters for points, comments, dates, author or domain. Use it to track mentions of a product on HN.

Examples: [Python](python/hacker_news_scraper.py) · [Node.js](nodejs/hacker-news-scraper.mjs) · Ready-made runs: [Track Hacker News stories about AI agents](https://apify.com/tamnt67/hacker-news-scraper/examples/hacker-news-ai-agent-stories)

### [Polymarket & Kalshi Odds Scraper ($1/1K markets)](https://apify.com/tamnt67/prediction-markets-scraper)

Polymarket and Kalshi odds scraper for prediction markets: question, outcome, implied probability, bid, ask, last price, 24h change, volume, liquidity and end date. Takes keywords, the sources to read and a minimum volume. Use it to track prediction market odds on elections, sports or economics.

Examples: [Python](python/prediction_markets_scraper.py) · [Node.js](nodejs/prediction-markets-scraper.mjs) · Ready-made runs: [Snapshot of Polymarket and Kalshi odds](https://apify.com/tamnt67/prediction-markets-scraper/examples/polymarket-kalshi-odds-snapshot) · [Bitcoin prediction market odds on Polymarket and Kalshi](https://apify.com/tamnt67/prediction-markets-scraper/examples/polymarket-kalshi-bitcoin-odds)

### [RSS Feed Reader: RSS, Atom & JSON Feed to JSON ($1/1K)](https://apify.com/tamnt67/rss-feed-reader)

RSS feed reader for RSS, Atom and JSON Feed items: title, link, author, publish date, categories, summary, full content and attachments. Takes feed URLs, or website URLs and finds their feed. Use it to collect news articles or blog posts into a dataset.

Examples: [Python](python/rss_feed_reader.py) · [Node.js](nodejs/rss-feed-reader.mjs) · Ready-made runs: [Combine several news RSS feeds into one dataset](https://apify.com/tamnt67/rss-feed-reader/examples/news-feeds-to-json)

### [Substack Posts Scraper: Likes, Comments, Full Text ($1/1K)](https://apify.com/tamnt67/substack-scraper)

Substack posts scraper: title, subtitle, author, publish date, free or paid, word count, likes, comments, restacks and full text of free posts. Takes Substack newsletter URLs, custom domains included. Use it to analyze a newsletter's archive and engagement.

Examples: [Python](python/substack_scraper.py) · [Node.js](nodejs/substack-scraper.mjs) · Ready-made runs: [Export the post archive of a Substack newsletter](https://apify.com/tamnt67/substack-scraper/examples/substack-newsletter-archive) · [Search a Substack newsletter's posts by keyword](https://apify.com/tamnt67/substack-scraper/examples/substack-search-posts) · [Find the most liked posts of a Substack newsletter](https://apify.com/tamnt67/substack-scraper/examples/substack-most-liked-posts)

## SEO and marketing

### [App Store Search Scraper: ASO Keyword Ranks ($1/1K apps)](https://apify.com/tamnt67/app-store-search-scraper)

App Store search scraper for ASO keyword rankings: rank, app name, developer, price, rating, rating count, genre, version, update date and description. Takes keywords and App Store countries. Use it to see which iOS apps rank for a keyword and track your app's rank.

Examples: [Python](python/app_store_search_scraper.py) · [Node.js](nodejs/app-store-search-scraper.mjs) · Ready-made runs: [Check App Store rankings for keywords in the US and UK](https://apify.com/tamnt67/app-store-search-scraper/examples/app-store-keyword-rankings-us-uk)

### [Domain WHOIS Lookup: expiry, registrar, age ($0.5/1K)](https://apify.com/tamnt67/domain-whois-rdap-scraper)

Domain WHOIS lookup over RDAP: registered flag, registrar, creation, expiry and update dates, days until expiry, domain age, status and nameservers. Takes a list of domain names. Use it to check domain expiry dates and domain availability in bulk.

Examples: [Python](python/domain_whois_rdap_scraper.py) · [Node.js](nodejs/domain-whois-rdap-scraper.mjs) · Ready-made runs: [Check expiry dates and registrars for a list of domains](https://apify.com/tamnt67/domain-whois-rdap-scraper/examples/domain-expiry-dates-bulk) · [Domain registrar and creation date lookup](https://apify.com/tamnt67/domain-whois-rdap-scraper/examples/domain-registrar-creation-date-lookup)

### [Google Autocomplete Keyword Scraper ($1/1K keywords)](https://apify.com/tamnt67/google-autocomplete-scraper)

Google Autocomplete keyword suggestions scraper: seed keyword, suggestion, modifier, position, word count, language and country. Takes seed keywords and expands them with A to Z and question words. Use it for SEO keyword research and long-tail keyword ideas.

Examples: [Python](python/google_autocomplete_scraper.py) · [Node.js](nodejs/google-autocomplete-scraper.mjs) · Ready-made runs: [Generate long-tail keyword ideas from Google Autocomplete](https://apify.com/tamnt67/google-autocomplete-scraper/examples/long-tail-keyword-ideas)

### [Google Trends Trending Now Scraper ($2/1K trends)](https://apify.com/tamnt67/google-trends-trending-scraper)

Google Trends trending searches scraper: keyword, rank, approximate search volume, start time and linked news stories. Takes a list of countries and reads the Google Trends Trending Now feed. Use it to spot daily trending topics and keywords in any country.

Examples: [Python](python/google_trends_trending_scraper.py) · [Node.js](nodejs/google-trends-trending-scraper.mjs) · Ready-made runs: [Get today's trending searches in the US, UK and India](https://apify.com/tamnt67/google-trends-trending-scraper/examples/google-trends-daily-us-uk-india) · [Google trending searches today in Southeast Asia](https://apify.com/tamnt67/google-trends-trending-scraper/examples/google-trends-southeast-asia-today)

## Developer tools

### [DNS Records Lookup: MX, SPF, DMARC, A, TXT ($0.5/1K)](https://apify.com/tamnt67/dns-records-lookup)

DNS records lookup: A, AAAA, CNAME, MX, NS, TXT, SOA and CAA records, plus mail provider, SPF record and DMARC policy. Takes a list of domains and queries public DNS over HTTPS. Use it to check MX records and email deliverability setup (SPF, DMARC) for many domains.

Examples: [Python](python/dns_records_lookup.py) · [Node.js](nodejs/dns-records-lookup.mjs) · Ready-made runs: [Find each company's email provider and SPF/DMARC setup](https://apify.com/tamnt67/dns-records-lookup/examples/email-provider-spf-dmarc-check) · [Bulk DNS lookup: A, MX and NS records](https://apify.com/tamnt67/dns-records-lookup/examples/bulk-dns-lookup-a-mx-ns)

### [GitHub Trending Repositories Scraper ($0.8/1K)](https://apify.com/tamnt67/github-trending-scraper)

GitHub trending repositories scraper: rank, repository name, owner, description, language, stars, forks, stars gained in the period and contributors. Takes periods (today, this week, this month) and programming languages. Use it to spot fast-growing open source projects.

Examples: [Python](python/github_trending_scraper.py) · [Node.js](nodejs/github-trending-scraper.mjs) · Ready-made runs: [See this week's trending Python repositories on GitHub](https://apify.com/tamnt67/github-trending-scraper/examples/github-trending-python-weekly) · [GitHub trending repositories this month](https://apify.com/tamnt67/github-trending-scraper/examples/github-trending-repositories-monthly)

### [HTTP Request Tool: GET/POST via Proxy ($1/1K requests)](https://apify.com/tamnt67/http-request-tool)

HTTP request tool: status code, headers, body, parsed JSON, final URL, redirects, size and response time for each request. Takes URLs with GET, POST, PUT, PATCH, DELETE or HEAD, custom headers, body and optional proxy country. Use it to call an API or check URLs from a workflow.

Examples: [Python](python/http_request_tool.py) · [Node.js](nodejs/http-request-tool.mjs) · Ready-made runs: [Check status codes and bodies of a list of URLs](https://apify.com/tamnt67/http-request-tool/examples/check-api-and-page-responses)

### [PDF Text Extractor: PDF URL to Text, per Page ($2/1K)](https://apify.com/tamnt67/pdf-text-extractor)

PDF text extractor: full text per PDF or per page, page count, word count, file size and metadata (title, author, dates). Takes PDF URLs, nothing to upload. Use it to turn PDF documents into text for search or LLM input.

Examples: [Python](python/pdf_text_extractor.py) · [Node.js](nodejs/pdf-text-extractor.mjs) · Ready-made runs: [Extract text from PDF links, page by page](https://apify.com/tamnt67/pdf-text-extractor/examples/pdf-to-text-by-page)

### [Website Screenshot: Full Page, PNG/JPEG, Bulk ($2.5/1K)](https://apify.com/tamnt67/website-screenshot)

Website screenshot capture with real Chrome: screenshot download link, page title, final URL, HTTP status, image size and format. Takes a list of URLs, full page or visible area, PNG or JPEG, any viewport width (desktop or mobile). Use it to archive web pages or check how sites render.

Examples: [Python](python/website_screenshot.py) · [Node.js](nodejs/website-screenshot.mjs) · Ready-made runs: [Take full-page screenshots of a list of websites](https://apify.com/tamnt67/website-screenshot/examples/full-page-website-screenshots)

## AI and documents

### [Image OCR: Image to Text, 100+ Languages ($3/1K)](https://apify.com/tamnt67/image-ocr)

Image OCR text extraction with Tesseract: recognized text, confidence score, line, word and character counts. Takes image URLs (screenshots, scans, receipts, labels, photos of text) and OCR languages, 100+ supported. Use it to turn images into text without an external OCR API.

Examples: [Python](python/image_ocr.py) · [Node.js](nodejs/image-ocr.mjs) · Ready-made runs: [Extract English text from images](https://apify.com/tamnt67/image-ocr/examples/image-text-extraction-english)

## Lead generation

### [App Store Reviews Scraper (iOS ratings, text, any country)](https://apify.com/tamnt67/app-store-reviews-scraper)

App Store reviews scraper for iOS apps: star rating, title, text, author, app version, helpful votes and date, plus app rating and developer. Takes app IDs or Apple App Store URLs and a list of countries. Use it to track iPhone app ratings and user feedback.

Examples: [Python](python/app_store_reviews_scraper.py) · [Node.js](nodejs/app-store-reviews-scraper.mjs) · Ready-made runs: [Collect iOS App Store reviews in the US and UK](https://apify.com/tamnt67/app-store-reviews-scraper/examples/app-store-reviews-us-uk) · [Export ChatGPT App Store reviews](https://apify.com/tamnt67/app-store-reviews-scraper/examples/chatgpt-app-store-reviews)

### [Google Ads Transparency Scraper (ads, advertisers, regions)](https://apify.com/tamnt67/google-ads-transparency-scraper)

Google Ads Transparency Center scraper for Google ads: advertiser name and ID, creative ID, ad format, first and last shown dates, image or preview link and ad URL. Takes advertiser names, AR IDs or website domains, with country, format and date filters. Use it to research competitor ads.

Examples: [Python](python/google_ads_transparency_scraper.py) · [Node.js](nodejs/google-ads-transparency-scraper.mjs) · Ready-made runs: [See which Google ads Nike runs in Germany](https://apify.com/tamnt67/google-ads-transparency-scraper/examples/competitor-google-ads-germany) · [See a competitor's Google ads in the US by domain](https://apify.com/tamnt67/google-ads-transparency-scraper/examples/competitor-ads-by-domain-us) · [List a competitor's video ads on Google](https://apify.com/tamnt67/google-ads-transparency-scraper/examples/competitor-video-ads)

### [Google Play Reviews Scraper (ratings, text, dev replies)](https://apify.com/tamnt67/google-play-reviews-scraper)

Google Play reviews scraper: star rating, review text, author, date, thumbs up, app version and developer reply. Takes package names or Play Store URLs, any country and language, with sort order and star filter. Use it to analyze Android app reviews and user feedback.

Examples: [Python](python/google_play_reviews_scraper.py) · [Node.js](nodejs/google-play-reviews-scraper.mjs) · Ready-made runs: [Analyze competitor app reviews on Google Play](https://apify.com/tamnt67/google-play-reviews-scraper/examples/google-play-competitor-app-reviews) · [Find 1-star reviews of an app on Google Play](https://apify.com/tamnt67/google-play-reviews-scraper/examples/google-play-negative-reviews) · [Collect Google Play reviews from India](https://apify.com/tamnt67/google-play-reviews-scraper/examples/google-play-reviews-india)

### [Skool Communities Scraper ($2/1K communities)](https://apify.com/tamnt67/skool-communities-scraper)

Skool communities scraper: name, URL, description, member count, paid flag, price, rating and review count. Takes search keywords for the public Skool discovery page. Use it to research Skool groups in a niche and their pricing.

Examples: [Python](python/skool_communities_scraper.py) · [Node.js](nodejs/skool-communities-scraper.mjs) · Ready-made runs: [Find paid and free Skool communities about AI automation](https://apify.com/tamnt67/skool-communities-scraper/examples/skool-ai-automation-communities)

### [Website Contact Scraper (emails, phones, social links)](https://apify.com/tamnt67/website-contact-scraper)

Website contact scraper: emails, phone numbers and social links (LinkedIn, Facebook, Instagram, X, YouTube, TikTok) for each site. Takes a list of domains or URLs and checks the homepage plus contact, about and imprint pages. Use it to build lead lists with email addresses from company websites.

Examples: [Python](python/website_contact_scraper.py) · [Node.js](nodejs/website-contact-scraper.mjs) · Ready-made runs: [Get public contact details from company websites](https://apify.com/tamnt67/website-contact-scraper/examples/company-website-contact-details) · [Find social media links of agency websites](https://apify.com/tamnt67/website-contact-scraper/examples/agency-websites-social-links)

### [Website Tech Stack Detector: CMS, Analytics ($3/1K)](https://apify.com/tamnt67/tech-stack-detector)

Website tech stack detector for website technologies: CMS, ecommerce platform, JavaScript framework, analytics, ad pixels, live chat, payments, CDN, hosting and server, with evidence. Takes a list of domains or URLs. Use it to find sites built with Shopify or WordPress for lead lists.

Examples: [Python](python/tech_stack_detector.py) · [Node.js](nodejs/tech-stack-detector.mjs) · Ready-made runs: [Detect the tech stack of e-commerce websites](https://apify.com/tamnt67/tech-stack-detector/examples/ecommerce-site-tech-stack)

### [Y Combinator Companies Scraper + Jobs ($1/1K)](https://apify.com/tamnt67/yc-companies-scraper)

Y Combinator companies scraper for YC startups: name, batch, status, industry, team size, location, website, social links and open jobs with salary ranges. Takes batches, industries, locations, keywords, status and a hiring-only switch. Use it to build startup lead lists or find YC jobs.

Examples: [Python](python/yc_companies_scraper.py) · [Node.js](nodejs/yc-companies-scraper.mjs) · Ready-made runs: [List YC startups from W25 and S25 that are hiring](https://apify.com/tamnt67/yc-companies-scraper/examples/yc-startups-hiring-w25-s25)

## Events and travel

### [Eventbrite Events Scraper: Venues, Dates, Prices ($2/1K)](https://apify.com/tamnt67/eventbrite-scraper)

Eventbrite events scraper: name, summary, start and end time, venue, address, coordinates, category, online flag and ticket link; details add price, free flag and organizer. Takes keywords and locations or Eventbrite search URLs. Use it to build local event calendars.

Examples: [Python](python/eventbrite_scraper.py) · [Node.js](nodejs/eventbrite-scraper.mjs) · Ready-made runs: [List upcoming tech events in New York on Eventbrite](https://apify.com/tamnt67/eventbrite-scraper/examples/eventbrite-new-york-tech-events)

## Automation

### [ESPN Scores Scraper: NBA, NFL, Soccer, Tennis ($2/1K)](https://apify.com/tamnt67/espn-scores-scraper)

ESPN scores scraper for live scores, results and schedules: teams, scores, period scores, status, venue, broadcasts and betting lines. Takes leagues (NBA, NFL, MLB, NHL, Premier League, Champions League, ATP, WTA and more) and dates. Use it to feed sports scores into apps or models.

Examples: [Python](python/espn_scores_scraper.py) · [Node.js](nodejs/espn-scores-scraper.mjs) · Ready-made runs: [Get yesterday's NBA and Premier League results](https://apify.com/tamnt67/espn-scores-scraper/examples/espn-yesterday-results-nba-premier-league) · [NFL scores and betting lines this week](https://apify.com/tamnt67/espn-scores-scraper/examples/espn-nfl-scores-odds-this-week)

### [Luma Events Scraper: Tech Meetups by City ($2/1K)](https://apify.com/tamnt67/luma-events-scraper)

Luma events scraper for lu.ma: name, URL, start and end time, city, venue, free or paid, ticket price, sold out, spots left, guest count and organizer. Takes cities and an optional keyword. Use it to find tech meetups, AI and startup events in a city.

Examples: [Python](python/luma_events_scraper.py) · [Node.js](nodejs/luma-events-scraper.mjs) · Ready-made runs: [List upcoming AI events in San Francisco on Luma](https://apify.com/tamnt67/luma-events-scraper/examples/luma-ai-events-san-francisco)

### [Yahoo Finance Historical Prices Scraper ($0.5/1K rows)](https://apify.com/tamnt67/yahoo-finance-history-scraper)

Yahoo Finance historical prices scraper for stock prices: date, open, high, low, close, adjusted close, volume, dividends and splits. Takes symbols of stocks, ETFs, indices, crypto or currency pairs, a date range and an interval. Use it to build OHLC price history for backtests or charts.

Examples: [Python](python/yahoo_finance_history_scraper.py) · [Node.js](nodejs/yahoo-finance-history-scraper.mjs) · Ready-made runs: [Download one year of daily prices for stocks and crypto](https://apify.com/tamnt67/yahoo-finance-history-scraper/examples/stock-crypto-price-history-1y) · [Bitcoin historical prices, daily, 5 years](https://apify.com/tamnt67/yahoo-finance-history-scraper/examples/bitcoin-historical-prices-daily) · [SPY ETF price history with dividends](https://apify.com/tamnt67/yahoo-finance-history-scraper/examples/spy-etf-price-history-dividends)

## Support

Found a problem or need a field that is missing? Open an issue on the tool's page on Apify (Issues tab) or in this repository.

## License

The example code in this repository is released under the MIT License.
