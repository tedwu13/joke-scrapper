from bs4 import BeautifulSoup
from pprint import pprint

import urllib
import lxml.html
import time


r = urllib.urlopen('http://www.laughfactory.com/jokes/popular-jokes').read()
soup = BeautifulSoup(r, "lxml")

start_time = time.time()

# Get all the urls from the side navigation bar

def get_jokes_nav_urls():
    print "Get URLS from Page................"
    urls = [] 
    for link in soup.find_all("div", {'class': 'jokes-nav'}):
        for l in link.find_all('a', href=True):
            urls.append(l.get('href'))
    print "URLS are..............."
    print urls
    return urls

def append_url_parameters(urls): 
    paramsArray = ['/1','/2','/3','/4','/5']
    urlArray = []
    for url in urls: 
        url += paramsArray[0]
        urlArray.append(url)
    print urlArray

def get_jokes():
    print "Start Scraping....."
    urls = get_jokes_nav_urls()

    append_url_parameters(urls)
    # urls = ['http://www.laughfactory.com/jokes/popular-jokes', 
    # 'http://www.laughfactory.com/jokes/latest-jokes']

    jokes = []
    for joke_url in urls:
        r = urllib.urlopen(joke_url).read()
        soup = BeautifulSoup(r, "lxml")
        joke_text = soup.find_all("div", {'class': 'joke-text'})
        for j in joke_text:
            for child in j.findChildren():
                jokes.append(child.text.strip().encode('utf-8'))
    print "HERE ARE ALL THE JOKES"
    pprint(jokes)

def scrape_data():
    get_jokes()

# Start main script
scrape_data()

end_time = time.time()
execution_time = end_time - start_time
print("Execution Time .... %s seconds......" %execution_time)
