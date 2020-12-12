from bs4 import BeautifulSoup
import requests


def build_url(min_bedrooms, max_bedrooms, city='cleveland', dogs_ok=1, cats_ok=1):
    domain = f'https://{city}.craigslist.org/search/apa?'
    url = f'{domain}min_bedrooms={min_bedrooms}&max_bedrooms={max_bedrooms}&availabilityMode=0&pets_cat={cats_ok}&pets_dog={dogs_ok}&sale_date=all+dates'
    return url


query_set = build_url(min_bedrooms=2, max_bedrooms=2)

# Getting the webpage, creating a Response object.
response = requests.get(query_set)

# Extracting the source code of the page.
data = response.text

# Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'lxml')

# Extracting all the <a> tags whose class name is 'result-title' into a list.
all_listings = soup.find('ul', {'class': 'rows'})
posts = soup.findAll('li', {'class': 'result-row'})
post_date = soup.findAll('time', {'class': 'result-date'})
title = soup.findAll('a', {'class': 'result-title'})
price = soup.find('span', {'class': 'result-price'})
url = soup.find('a', href=True)
info = soup.find('div', {'class': 'result-info'})
