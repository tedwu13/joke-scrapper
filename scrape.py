from bs4 import BeautifulSoup
import urllib
import lxml.html

r = urllib.urlopen('http://www.laughfactory.com/jokes/popular-jokes').read()
soup = BeautifulSoup(r, "lxml")

# Get all the urls from the side navigation bar

def get_jokes_nav_urls():
    urls = [] 
    for link in soup.find_all("div", {'class': 'jokes-nav'}):
        for l in link.find_all('a', href=True):
            urls.append(l.get('href'))
    return urls

def set_scraping_url():
    print "Starting scraping process....."
    # urls = get_jokes_nav_urls()
    urls = ['http://www.laughfactory.com/jokes/popular-jokes', 
    'http://www.laughfactory.com/jokes/latest-jokes']

    jokes = []
    for joke_url in urls:
        r = urllib.urlopen(joke_url).read()
        soup = BeautifulSoup(r, "lxml")
        # print select(soup, 'div.joke-text p')
        joke_text = soup.find_all("div", {'class': 'joke-text'})
        for j in joke_text:
            for child in j.findChildren():
                jokes.append(child.text.strip().encode('utf-8'))
set_scraping_url();