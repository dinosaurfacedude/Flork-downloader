#! usr/bin/env python3
#written by Daniel Jones
#purpose: downloads the 10 newest Flork of Cows comics from reddit.com
#limits: only works with *nix systems.


#libraries
import praw
import urllib.request
import os
import pwd

#gets username for linux user
user = pwd.getpwuid( os.getuid() )[ 0 ]

#logon information
reddit = praw.Reddit(
client_id='14 digit ID here', \
client_secret = '27 digit ID here', \
user_agent = 'user agent name here', \
username='reddit username here no /u/', \
password='password goes here'
)


#flork of cows subreddit
sub = reddit.subreddit("florkofcowsofficial")

#downloads newest posts
top_subreddit = sub.new(limit=10)

for submission in top_subreddit:
	
	filename = submission.title
	myurl = submission.url
	
	#saves in pictures folder in directory 'Flork.'
	#If using windows, just edit this line to get your filepath.
	saveplace = "/home/" + user + "/Pictures/Flork/" + filename + ".jpg"

	urllib.request.urlretrieve(myurl, saveplace)

	print("downloaded ", filename," from ", myurl, "\n")
