import requests

from bs4 import BeautifulSoup

# url = 'http://github.com'
url = 'https://www.nytimes.com/'
req = requests.get(url)
req_html = req.text
print(req_html)

# some requests code here for getting r_html 

soup = BeautifulSoup(req_html)
title = soup.find('span', 'articletitle').string
