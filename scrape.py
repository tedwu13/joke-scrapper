from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://www.laughfactory.com/jokes/popular-jokes').read()
soup = BeautifulSoup(r)
jokes = soup.find_all("div", {'class': 'joke-test'})


# Get all the jokes-nav urls

def get_jokes_nav_urls():
    urls = [] 
    for link in soup.find_all("div", {'class': 'jokes-nav'}):
        for l in link.find_all('a', href=True):
            urls.append(l.get('href'))
    return urls
def set_scraping_url():
    urls = get_jokes_nav_urls()
    
    # for joke_url in urls:
        # data = urllib.urlopen(joke_url).read()
    # print links

set_scraping_url();