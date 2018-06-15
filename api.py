
import hug, mysql.connector, json, collections, requests

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="base_pokemon"
)

cursor = conn.cursor()

@hug.get('/pokemon/all')
@hug.format.content_type('sorted_json')
def list():
    """Affichage de tous les pokemon de la base de donnees"""
    cursor.execute("SELECT * FROM pokemon")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()

    return rows

@hug.post('/pokemon/add')
def ajouter(body, request, response):

    """ Cette fonction permet d'ajouter un pokemon dans la base de donnees """

    cursor.execute("INSERT INTO pokemon (pki, name, type, total, hp, attack, defense, sp_atk, sp_def, speed) "
                   "VALUES (%(pki)s, %(name)s, %(type)s, %(total)s, %(hp)s, %(attack)s, %(defense)s, %(sp_atk)s, %(sp_def)s, %(speed)s)", body)
    conn.commit()
    conn.close()

    return json.dumps("L'enregistrement a bien été effectué")


@hug.put('/pokemon/update/{id}')
def modifier(id: hug.types.number, body):
    """Cette fonction permet la modification d'un pokemon"""
    cursor.execute("""UPDATE pokemon SET (pki = %(pki)s, name = %(name)s, type = %(type)s, total = %(total)s, hp = %(hp)s, attack = %(attack)s, 
                      defense = %(defense)s, sp_atk = %(sp_atk)s, sp_def = %s, speed = %(sp_def)s WHERE id= {id}""", body)
    conn.commit()
    conn.close()

    return json.dumps("Modification réussie")

@hug.delete('/pokemon/delete/{id}')
def supprimer(id: hug.types.number):
    """Fonction permettant de supprimer un pokemon à partir de son ID"""
    cursor.execute("""DELETE FROM pokemon WHERE id = %s""", [id])

    conn.commit()
    conn.close()

    return json.dumps("Vous venez de Supprimer le pokemon {id} de la base de données")