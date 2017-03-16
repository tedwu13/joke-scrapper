from bs4 import BeautifulSoup
from pprint import pprint

import urllib


def scrapeMainUrl(): 
    r = urllib.urlopen('http://www.kickvick.com/stupid-funny-jokes/').read()
    soup = BeautifulSoup(r, "lxml")

    print "Get images from Page................"
    images = []

    for link in soup.find_all("p"):
        for l in link.find_all('a', href=True):
            images.append(l.get('href'))
    
    print "Images are..............." + images
    return images

def downloadImage():

def scrape_data():
    images = scrapeMainUrl()

# Start main script
def main():
    images = scrapeMainUrl()
    downloadImage(images)

if __name__ == '__main__':
 # execute only if run as the entry point into the program
 main()

