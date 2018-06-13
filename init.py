#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup


url = "https://pokemondb.net/pokedex/all"
response = requests.get(url)
html = str(response.content)

soup = BeautifulSoup(html, "html.parser")

tab = soup.find(id="pokedex")

for link in tab.find_all("tr"):
    print(len(tab.find_all("td")))

    for l in tab.find_all("td"):
        print(l.text, end=" ")

    print("\n")
