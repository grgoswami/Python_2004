import requests

from bs4 import BeautifulSoup

# credit: https://medium.com/@ProxiesAPI.com/scraping-the-new-york-times-with-python-and-beautiful-soup-6e5f3bc58e39

url = 'https://www.nytimes.com/'
response = requests.get(url) 
print(response.content)

# This example is hard to make sense but it's a baby 'news aggregator'
soup = BeautifulSoup(response.content,'lxml')
for item in soup.select('.assetWrapper'):
    #print(item)
    div = item.find('div')
    h2 = item.find('h2')    
    #print(div)
    if h2 is not None:
        print(h2.get_text())
        print(72 * '-')
    if div is not None:
        print(div.get_text())
        print('\n\n')
        
        
