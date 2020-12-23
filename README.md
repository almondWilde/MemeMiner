# MemeScraper<br />
MemeScraper is a system for collecting memes from social media and displaying the memes in a web interface.<br />
<br />
![Flowchart](https://github.com/almondWilde/MemeScraper/blob/main/memescraper_flowchart.jpg)<br />
## I. Memescraper Server ![Server Code](https://github.com/almondWilde/MemeScraper/tree/main/scraper)<br /><br />
  ### Specs and System Dependencies<br />
    1. NVIDIA - for performance over CPU-only and compatibility with python ML libraries in dedupe() and cluster()<br />
    2. Python3<br />
    3. Putty/OpenSSH - for upload() to upload the clustered image set to the web server<br />
  ### B. Functions<br />
    1. getMemes()<br />
      a. uses scraping algorithms to get memes from instagram<br />
        i. other social media sites could be scraped and may even be more reliable<br />
      b. access to the web over http/https<br />
      c. access to the meme storage<br />
    2. dedupe()<br />
      a. De-Duplicating, or deduping, the Meme Storage using ![knjcode/imgdedupes](https://github.com/knjcode/imgdupes)<br />
      b run after getMemes() to control for duplicate images which may pollute the image set<br />
    3. clustering()<br />
      a. sorts the Meme Storage using ![/rohanbaisantry/image-clustering](https://github.com/rohanbaisantry/image-clustering)<br />
      c. output: n clusters (as directories) of m memes randomly chosen from the Meme Storage<br />
        i. currently n=10 and m=5000 (~500 MB)<br />
    4. upload()<br />
      a. uploads an m memes payload to the web server through SCP<br />
      b. compress the payload before uploading<br />
  ### C. Meme Storage<br />
    1. Stores all collected memes<br />
    2. local directory Storage<br />
    3. accessed by getMemes(), dedupe(), and clustering()<br />
  ### D. Scheduled Processes<br />
    1. getMemes weekly<br />
    2. cluster and upload a new meme payload nightly<br />
      i. the Memes Storage should be large to minimize repeating memes two nights in a row<br />
    3. Cronjobs in Linux<br />
## II. Web Server<br />
  ### A. NGINX<br />
  ### B. PHP - for image handlng<br />
  ### C. SSH - backdoor for MemeScraper<br />
## III. Flow - Bash in the root directory<br />
    1. getMemes from the public internet and store them in Meme Storage<br />
    2. deduplicate Meme Storage<br />
    3. cluster m memes from Meme Storage<br />
    4. upload the m meme payload to the web server<br />
    5. dynamically display the memes on an NGINX web server<br />
<br />
![ERD](https://github.com/almondWilde/MemeScraper/blob/main/MemeScraper_ERD.jpg)<br />
<br />
