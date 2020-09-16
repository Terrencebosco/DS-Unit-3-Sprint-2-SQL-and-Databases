import json
import sqlite3
import os
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import execute_values

# step one: set file path
DB_path = "/home/terrence/Documents/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), DB_path)

# step two: set connection
connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION", connection)

# step 3: set cursor
cursor = connection.cursor()
print("CURSOR", cursor)

# pull in data from local file 
query1 = 'SELECT name, level FROM charactercreator_character'
data = cursor.execute(query1).fetchall()

# loaded into .env for security 
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection2 = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print('CONNECTION', connection2)

cursor2 = connection2.cursor()
print('CURSER', cursor2)

# maki new table with psycopg2 to online server
new_table = """
CREATE TABLE IF NOT EXISTS rpg_test (
name VARCHAR(30),
level INTEGER NOT NULL
);
"""
cursor2.execute(new_table)
connection2.commit()

# syntax works for entering data
insertion_query = "INSERT INTO rpg_test (name, level) VALUES %s"
execute_values(cursor2, insertion_query, [
('test', 1)
])
connection2.commit()

# moving data from rpg query search to my_list to pass to new table 
my_list = []
for i in data:
    my_list.append(i)

# pass data using psycopg2
insert_query = "INSERT INTO rpg_test (name, level) values %s"
execute_values(cursor2, insert_query, my_list)
connection2.commit()

############# remember that these have to be sepereated ########
query2 = "SELECT * FROM rpg_test"
cursor2.execute(query2) 
result2 = cursor2.fetchall() 

# always close at the end
if(connection2):
    cursor2.close()
    connection2.close()
    print("PostgreSQL connection is closed")

