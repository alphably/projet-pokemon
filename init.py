#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup


import mysql.connector, random

conn = mysql.connector.connect(host="localhost",user="root",password="", database="mydb")
cursor = conn.cursor()

def createTable():
    cursor.execute("""
      CREATE TABLE IF NOT EXISTS pokenom
      (
         id INT PRIMARY KEY AUTO_INCREMENT,
         pki VARCHAR(10),
         name VARCHAR(100),
         size ENUM('Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying',
          'Psychic', 'Bug', 'Rock','Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy'),
         total INT(5),
         hp INT(5),
         attack INT(5),
         defense INT(5),
         sp_atk INT(5),
         sp_def(5),
         speed(5),
      );
      """)





#url = "https://pokemondb.net/pokedex/all"
#response = requests.get(url)
#html = str(response.content)

# Mise en cache de la page HTML
#fichier = open("pokemon.html", "a")
#fichier.write(html)
#fichier.close()

#soup = BeautifulSoup(html, "html.parser")
with open("pokemon.html") as fp:
    soup = BeautifulSoup(fp)

tab = soup.find(id="pokedex")

for link in tab.find_all("tr"):
    print(len(tab.find_all("td")))

    for l in tab.find_all("td"):
        print(l.text, end=" ")

    print("\n")
