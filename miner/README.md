# Meme Scraper
Scrapes, Sorts, Loads memes

# To-do
## add instagram-scraper script here
  - [x] scrape from user list (add ig-users.txt here)
  - [x] scrape from memes tag
    - [x] save other encountered meme tags for later scraping
## dedupe & clustering image set
  - [x] find a working deduping algorithm
  - [ ] cluster deduped image set
## upload image clusters to web server
  - [ ] send image-clustering output folder to web server
## add a bash script to schedule processes
  - [ ] Linux miner script: get memes, dedupe, cluster
  - [ ] windows miner script
  - [ ] setup.sh
  1. scrape - passing
    - fine tuning
      - [ ] add a rate controller to limit the amount of requests sent
      - [ ] rotate tags list
      - [ ] track dead users
  2. dedupe
  3. cluster
  4. upload
