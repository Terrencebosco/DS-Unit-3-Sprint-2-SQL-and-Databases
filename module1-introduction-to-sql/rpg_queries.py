import os 
import sqlite3

# step one: set file path
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

# step two: set connection
connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION", connection)

# step 3: set cursor
cursor = connection.cursor()
print("CURSOR", cursor)

# step 4: make queries

query1 = 'SELECT count(distinct character_id) FROM charactercreator_character' #(302)

query2 = 'SELECT count(distinct name) FROM charactercreator_character'

query3 = 'SELECT count(distinct character_ptr_id) from charactercreator_cleric'

query4 = 'SELECT count(distinct character_ptr_id) from charactercreator_fighter'

query5 = 'SELECT count(distinct character_ptr_id) from charactercreator_mage'


query7 = 'SELECT count(distinct mage_ptr_id) from charactercreator_necromancer'

query8 = 'SELECT count(distinct character_ptr_id) from charactercreator_theif'

query9 = 'SELECT count(distinct item_id) FROM armory_item'

# figure out how to do in sql
query10 = '172 total items - 37 total weapons = 135(not weapons)'

query11 = '''
SELECT 
	armory_item.item_id,
    armory_item.name,
	armory_weapon.item_ptr_id 
FROM armory_weapon
JOIN armory_item ON armory_item.item_id = armory_weapon.item_ptr_id
'''

query12 = '''
SELECT
	charactercreator_character.character_id
	,count(charactercreator_character_inventory.item_id) as item_count
FROM charactercreator_character_inventory
JOIN charactercreator_character ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
GROUP BY charactercreator_character.character_id
LIMIT 20
'''


query13 = '''
SELECT 
	charactercreator_character.character_id
	,count(armory_weapon.item_ptr_id) as weapon_count
FROM charactercreator_character
LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character.character_id
LIMIT 20
'''

query14 = '''
SELECT AVG(item_count)
FROM(
	SELECT
	    charactercreator_character.character_id
	    ,count(charactercreator_character_inventory.item_id) as item_count
	FROM charactercreator_character_inventory
	JOIN charactercreator_character ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
	GROUP BY charactercreator_character.character_id
    )
'''

query15 = '''
SELECT AVG (weapon_count)
FROM(
	SELECT 
		charactercreator_character.character_id
		,count(armory_weapon.item_ptr_id) as weapon_count
	FROM charactercreator_character
	LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
	LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
	GROUP BY charactercreator_character.character_id
    )
'''


# step 5/6: exicute query, fetch data
result = cursor.execute(query15).fetchall()
print('RESULT', result)

# make a list the itter for all queries
my_query_list = [
'SELECT count(distinct character_id) FROM charactercreator_character',
'SELECT count(distinct name) FROM charactercreator_character',
'SELECT count(distinct character_ptr_id) from charactercreator_cleric',
'SELECT count(distinct character_ptr_id) from charactercreator_fighter',
'SELECT count(distinct character_ptr_id) from charactercreator_mage',
'SELECT count(distinct mage_ptr_id) from charactercreator_necromancer',
'SELECT count(distinct character_ptr_id) from charactercreator_thief',
'SELECT count(distinct item_id) FROM armory_item',
#'172 total items - 37 total weapons = 135(not weapons)',
'''
SELECT 
	armory_item.item_id,
    armory_item.name,
	armory_weapon.item_ptr_id 
FROM armory_weapon
JOIN armory_item ON armory_item.item_id = armory_weapon.item_ptr_id
''',
'''
SELECT
	charactercreator_character.character_id
	,count(charactercreator_character_inventory.item_id) as item_count
FROM charactercreator_character_inventory
JOIN charactercreator_character ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
GROUP BY charactercreator_character.character_id
LIMIT 20
''',
'''
SELECT 
	charactercreator_character.character_id
	,count(armory_weapon.item_ptr_id) as weapon_count
FROM charactercreator_character
LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character.character_id
LIMIT 20
''',
'''
SELECT AVG(item_count)
FROM(
	SELECT
	    charactercreator_character.character_id
	    ,count(charactercreator_character_inventory.item_id) as item_count
	FROM charactercreator_character_inventory
	JOIN charactercreator_character ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
	GROUP BY charactercreator_character.character_id
    )
''',
'''
SELECT AVG (weapon_count)
FROM(
	SELECT 
		charactercreator_character.character_id
		,count(armory_weapon.item_ptr_id) as weapon_count
	FROM charactercreator_character
	LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
	LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
	GROUP BY charactercreator_character.character_id
    )
'''
]

# print results after making a list of all queries
for i in my_query_list:
    result = cursor.execute(i).fetchall()
    print('RESULT', result)