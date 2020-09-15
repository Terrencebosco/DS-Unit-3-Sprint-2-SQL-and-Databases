import os
from dotenv import load_dotenv
import psycopg2

load_dotenv() #> loads contents of the .env file into the script's environment

# loaded into .env for security 
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

### Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print('CONNECTION', connection)

### A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor()
print('CURSER', cursor)

### An example query
cursor.execute('SELECT * from test_table;')

### Note - nothing happened yet! We need to actually *fetch* from the cursor
result = cursor.fetchall()
print(result)

#### in sqlite we can chain exicute and fetch ####

# insert data to the tabel

insert_query = '''
INSERT INTO test_table (name, data) VALUES
(
  'A row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
'''

###################### new to psycopg3 #####################

# run the query
cursor.execute(insert_query)

# commit the query 
connection.commit()

# close the cursor
cursor.close()

# close the connection
connection.close()

# print the new 
result = cursor.fetchall()
print(result)