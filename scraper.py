import requests
import praw
from bs4 import BeautifulSoup
import urllib.request
import os
import sys

r = praw.Reddit(user_agent='tensorflow_test')

posts = r.get_subreddit('earthporn').get_top_from_all(limit=200)

links = [x.url for x in posts]

for index, link in enumerate(links):
    if link[-4:] is not ".jpg":
        link += ".jpg"
    try:
        resource = urllib.request.urlopen(link)
        name = '%04d' % index
        output = open('data/%s.jpg' % name, "wb")
        output.write(resource.read())
        output.close()
    except:
        pass

