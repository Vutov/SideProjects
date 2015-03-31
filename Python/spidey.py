import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = 'http://bg04b.eu/'

urls = [url]
visited = [url]
# Gets page's HTML
while len(urls) > 0:
    try:
        htmlText = requests.get(urls[0]).text
    except:
        print(urls[0])
    # print(htmlText)
    soup = BeautifulSoup(htmlText)
    # Remove visited page from all stack
    urls.pop(0)
    # Find all <a> tags with value of href
    for link in soup.findAll('a', href=True):
        # print (link['href'])
        # Normalize urls
        normalizedUrl = urljoin(url, link['href'])
        # print(normalizedUrl)
        # Check if already visited and is proper part of the site
        if url in normalizedUrl and normalizedUrl not in visited:
            urls.append(normalizedUrl)
            visited.append(normalizedUrl)
    # Just to have some info
    print(len(urls))
print(visited)