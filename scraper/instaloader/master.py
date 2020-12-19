from instaloader import Instaloader
from instaloader.structures import Profile
import sys
import inquirer
import getpass

def login(user, passwd, loader=Instaloader()):
	loader = loader
	user = input('Username: ' )
	passwd = getpass.getpass('Password: ')
	loader.login(user=user,passwd=passwd)

loader = Instaloader()
#loader.context.username='theemptytrashbag'
loader.login(user='theemptytrashbag', passwd='8utt3r_5c0tch')

loader.download_comments=False

#input meme tags from a file
try:
	with open('meme-tags.txt', 'r') as meme_tags:
		visited = []
		for tag in meme_tags:
			tag.replace('\n', '')
			#check if the visited list works
			if tag not in visited and not (tag == ''):
				visited.append(tag)
				loader.download_hashtag(tag, max_count=100, profile_pic=False)
				print(visited)
except Exception as e:
	print(e)
with open('meme-tags.txt', 'w') as meme_tags:
	#reset meme tags doc
	#each run of the script will be a new seed for tag propogation
	meme_tags.write('memes')