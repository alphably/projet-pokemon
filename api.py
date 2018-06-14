"""A basic (single function) API written using hug"""
import hug, mysql.connector, json, collections
conn = mysql.connector.connect(host="localhost",user="root", password="", database="base_pokemon")
cursor = conn.cursor()

@hug.get('/')
@hug.format.content_type('sorted_json')
def pokemon_list():
    """Says happy birthday to a user"""
    cursor.execute("SELECT * FROM pokemon")
    rows = cursor.fetchall()
    
    # champ = ['id','pki', 'name', 'type', 'total', 'hp', 'attack', 'defense', 'sp_atk', 'sp_def', 'speed']
    # objects_list = []
    # for row in rows:
    #     #print(row)
    #     i = 0
    #     for r in row:
    #
    #         print(r)
    #         d = collections.OrderedDict()
    #         d[champ[i]] = row
    #
    # # SQL SELECT
    # # retourner
    #
    # exit()
    return json.dumps(rows)

def groupe_list():
    """Says happy birthday to a user"""

    # SQL SELECT
    # retourner
    return "Bienvenue sur la page d'accuiel"

# ajout des information
@hug.post('/')
def home():
    """Says happy birthday to a user"""

    return "Bienvenue sur la page d'accuiel"


# modifier un exitant
@hug.put('/')
def home():
    """Says happy birthday to a user"""

    return "Bienvenue sur la page d'accuiel"


@hug.delete('/')
def home():
    """Says happy birthday to a user"""

    return "Bienvenue sur la page d'accuiel"