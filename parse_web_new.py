# %%
import csv

import requests
from bs4 import BeautifulSoup


"""
Parse data from news.tut.by
"""

url = 'https://news.tut.by/?sort=reads#sort'
page = requests.get(url)

# %%
soup = BeautifulSoup(page.text, 'html.parser')

news = soup.findAll('div', class_='news-entry small pic views ni')

news_data = []

for new in news:
    head = new.find('span', class_='entry-head _title').text
    comments_count = int(new.find('span', class_='entry-count').text) if new.find('span', class_='entry-count') else 0
    category = new.find('span', class_='entry-cat').text
    views = int(new.find('span', class_='entry-views').text.replace('\u2009', ''))
    link = new.find('a', class_='entry__link').attrs['href']

    news_data.append([head, comments_count, category, views, link])

with open('news.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['head', 'comments_count', 'category', 'views', 'link'])
    writer.writerows(news_data)

