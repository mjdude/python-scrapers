# https://medium.com/@dawran6/twitter-scraper-tutorial-with-python-requests-beautifulsoup-and-selenium-part-2-b38d849b07fe
import requests
from bs4 import BeautifulSoup

url = 'https://twitter.com/search?q='
query = '%40dawranliou'

r = requests.get(url + query)
soup = BeautifulSoup(r.text, 'html.parser')

tweets = [p.text for p in soup.find_all('p', class_='tweet-text')]

print(tweets)