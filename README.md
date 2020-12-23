# MemeScraper
MemeScraper is a system for collecting memes from social media and displaying the memes in a web interface.

![Flowchart](https://github.com/almondWilde/MemeScraper/blob/main/memescraper_flowchart.jpg)
## I. Memescraper Server [Server Code](https://github.com/almondWilde/MemeScraper/tree/main/scraper)
  ### Specs and System Dependencies
    1. NVIDIA - for performance over CPU-only and compatibility with python ML libraries in dedupe() and cluster()
    2. Python3
    3. Putty/OpenSSH - for upload() to upload the clustered image set to the web server
  ### B. Functions
    1. getMemes()
      a. uses scraping algorithms to get memes from instagram
        i. other social media sites could be scraped and may even be more reliable
      b. access to the web over http/https
      c. access to the meme storage
    2. dedupe()
      a. De-Duplicating, or deduping, the Meme Storage using [knjcode/imgdedupes](https://github.com/knjcode/imgdupes)
      b run after getMemes() to control for duplicate images which may pollute the image set
    3. clustering()
      a. sorts the Meme Storage using [/rohanbaisantry/image-clustering](https://github.com/rohanbaisantry/image-clustering)
      c. output: n clusters (as directories) of m memes randomly chosen from the Meme Storage
        i. currently n=10 and m=5000 (~500 MB)
    4. upload()
      a. uploads an m memes payload to the web server through SCP
      b. compress the payload before uploading
  ### C. Meme Storage 
    1. Stores all collected memes
    2. local directory Storage
    3. accessed by getMemes(), dedupe(), and clustering()
  ### D. Scheduled Processes
    1. getMemes weekly
    2. cluster and upload a new meme payload nightly
      i. the Memes Storage should be large to minimize repeating memes two nights in a row
    3. Cronjobs in Linux
## II. Web Server [Server Code](https://github.com/almondWilde/MemeScraper/tree/main/)
  ### Specs
    1. NGINX
    2. PHP - for image handlng
    3. SSH - backdoor for MemeScraper
## III. Flow - Bash in the root directory
    1. getMemes from the public internet and store them in Meme Storage
    2. deduplicate Meme Storage
    3. cluster m memes from Meme Storage
    4. upload the m meme payload to the web server
    5. dynamically display the memes on an NGINX web server

![ERD](https://github.com/almondWilde/MemeScraper/blob/main/MemeScraper_ERD.jpg)

