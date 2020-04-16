import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint
import csv

s = requests.Session()
s.headers.update({
    'Referer': 'http://www.kinopoisk.ru',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
})

url = "https://www.kinopoisk.ru/top/"
page = s.get(url)

soup = BeautifulSoup(page.text, "html.parser")

films = []
for id in range(1, 251):  # (1, 251)
    film = soup.find('tr', id=f"top250_place_{id}")

    name = film.find('a', class_='all').text
    rating = float(film.find('a', class_='continue').text)
    votes = film.find('span', style="color: #777").text

    votes = int(votes.split()[0][1:])

    films.append((name, rating, votes))

pprint(films)


def write_data_to_csv(csv_filename: str, data_: list):
    with open(csv_filename, 'w') as file:
        writer = csv.writer(file)
        for row_ in data_:
            writer.writerow(row_)


write_data_to_csv('films.csv', films)

