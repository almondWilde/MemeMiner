import instagram_scraper as insta

scraper = insta.InstagramScraper(login_user='theemptytrashbag',
 login_pass='8utt3r_5c0tch', filename='ig-users.txt', interactive = True,
 quiet=False, maximum = 0, media_metadata=True, log_destination='logs/',
  latest=True, latest_stamps=True)

scraper.authenticate_with_login()
scraper.scrape()

scraper.logout()
#scraper.scrape_hashtag()
print(scraper.username)
