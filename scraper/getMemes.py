import os

os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
import instagram_scraper as insta


scraper = insta.InstagramScraper(login_user='theemptytrashbag', login_pass='8utt3r_5c0tch', filename='ig-users.txt', interactive = True, quiet=False, maximum = 500, media_metadata=True, log_destination='logs/', latest=True)
with open(scraper.filename, "r") as userf:
    scraper.usernames = userf.readlines()
scraper.usernames = [x.strip() for x in scraper.usernames]

if scraper.login_user and scraper.login_pass:
    print("pre-auth")
    scraper.authenticate_with_login()
    print("post auth")
else:
    print("guest user")
    scraper.authenticate_as_guest()

if scraper.tag:
    print("tag")
    scraper.scrape_hashtag()
elif scraper.location:
    print("scrape loc")
    scraper.scrape_location()
elif scraper.search_location:
    print("search tag")
    scraper.search_locations()
else:
    print("basic scrape")
    scraper.scrape()

scraper.save_cookies()
print("logging out")
scraper.logout()
#scraper.scrape_hashtag()
print(scraper.login_user)
