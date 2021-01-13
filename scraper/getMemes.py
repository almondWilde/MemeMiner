#run on ubuntu
import os

os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
import instagram_scraper as insta

#quiet but keeps Logs
#100 posts per Scraping
scraper = insta.InstagramScraper(login_user='memescraperproject', login_pass='******enter password here*******', interactive = False, quiet=False, maximum = 1, media_metadata=True, log_destination='logs/', latest=True)


if scraper.login_user and scraper.login_pass:
    print("pre-auth")
    scraper.authenticate_with_login()
    print("post auth")
else:
    print("guest user")
    scraper.authenticate_as_guest()

#this loop will scrape by tags first then users
for medium in ('t', 'u'):
    #assign the input file
    if medium == 'u':
        print("User input file: ig-users.txt")
        scraper.tag=False
        scraper.filename='ig-users.txt'
    if medium == 't':
        print("Tag input file: meme-tags.txt")
        scraper.tag = True
        scraper.filename = "meme-tags.txt"


    with open(scraper.filename, "r") as userf:
        scraper.usernames = userf.readlines()
    scraper.usernames = [x.strip() for x in scraper.usernames]

    if scraper.tag:
        print("Scraping by tag file...")
        scraper.scrape_hashtag()
    else:
        print("Scraping by user file...")
        #some users aren't scraped correctly
        scraper.scrape()

scraper.save_cookies()
print("logging out")
scraper.logout()
#scraper.scrape_hashtag()
print(scraper.login_user)
