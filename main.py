import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
# url to scrape
url = "https://www.morele.net/kategoria/karty-graficzne-12/,,,,,,,p,0,,,,/1/"

results = requests.get(url)

soup = BeautifulSoup(results.text, "html.parser")

Karta = []
Cena = []
# find products
Karta_div = soup.find_all('div', class_='cat-product-content')

for cards in Karta_div:
    name = cards.p.a.text
    Karta.append(name)

    price = cards.find('div', class_='price-new').text
    Cena.append(price)
# make a dataframe
Cards = pd.DataFrame({
    'Karta': Karta,
    'Cena': Cena,
})
# convert to string
Cards['Karta'] = Cards['Karta'].astype(str)
# Cards['Cena'] = Cards['Cena'].str.extract('(\d+)').astype(float)
# print output + datatypes
print(Cards)
print(Cards.dtypes)
# export output to a csv file
Cards.to_csv('GPUs.csv')
