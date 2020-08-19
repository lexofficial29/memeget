import praw
import requests
import time

reddit = praw.Reddit(client_id='CLIENT ID GOES HERE',
		     client_secret='SECRET TOKEN GOES HERE',
		     user_agent='my user agent')
used = []

while True:
	try:
		for submission in reddit.subreddit('memes').new(limit=1):
			url = submission.url_overridden_by_dest
			if (url in used):
				pass
			else:
				response = requests.get(url)
				title = submission.title + " - " + submission.url_overridden_by_dest.split("/")[-1]
				file = open(title,"wb")
				file.write(response.content)
				file.close()
				used.append(url)
				print("Downloaded ==> %s, with title ==> %s" %(url, submission.title))
			time.sleep(0.2)
	except:
		print("Failed to download")
