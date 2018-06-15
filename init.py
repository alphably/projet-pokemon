#!/usr/bin/python3

from bs4 import BeautifulSoup
import mysql.connector, random, requests

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="base_pokemon"
 )
cursor = conn.cursor()


def scriptSQL():
    cursor.execute("""CREATE DATABASE IF NOT EXISTS base_pokemon; """)

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS pokemon
      (
             id INT PRIMARY KEY AUTO_INCREMENT,
             pki VARCHAR(10),
             name VARCHAR(100),
             total INT(5),
             hp INT(5),
             attack INT(5),
             defense INT(5),
             sp_atk INT(5),
             sp_def INT(5),
             speed INT(5)
      );
  """)

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS type
     (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100)
     );
     """)

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS pokemon_type (
          pokemon_id int NOT NULL,
          type_id int NOT NULL,
          PRIMARY KEY (pokemon_id, type_id)
      )
    """)


scriptSQL()

#url = "https://pokemondb.net/pokedex/all"
#response = requests.get(url)
#html = str(response.content)

# Mise en cache de la page HTML
#fichier = open("pokemon.html", "a")
#fichier.write(html)
#fichier.close()

#soup = BeautifulSoup(html, "html.parser")


# recuperation du fichier pokemon
#soup = None
#
# fichier = open("pokemon.html", "r")
# soup = BeautifulSoup(fichier.read())
# fichier.close()

with open("pokemon.html") as fp:
    html_doc = fp.read()
#print(html_doc)

soup = BeautifulSoup(html_doc, "html.parser")

#print(soup)
#soup = BeautifulSoup("<html>data</html>")
type = soup.find(id="filter-pkmn-type")
tab = soup.find(id="pokedex")
#print(dir(type.find-all("option")))
dataTypeTemp = []
for o in type.find_all("option"):
    #print(o.text)
    dataTypeTemp.append(o.text)


dataType = dataTypeTemp[1:]
print(dataType)

for x in range(0, len(dataType)):
    cursor.execute("INSERT INTO type (name) VALUES (%s)", [dataType[x]])

conn.commit()
conn.close()
exit()

for link in tab.find_all("tr"):
    tt = []
    for l in link.find_all("td"):
        tt.append(l.text)

    nn = tt[:2] + tt[3:]

    if len(tt) > 0:
        print(tt[2])
        #exit()
        cursor.execute("INSERT INTO pokemon (pki, name, total, hp, attack, defense, sp_atk, sp_def, speed) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", nn)




