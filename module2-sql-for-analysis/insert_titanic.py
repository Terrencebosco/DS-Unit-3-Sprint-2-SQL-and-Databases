import json
import sqlite3
import os
import psycopg2
import pandas
import csv
from dotenv import load_dotenv
from psycopg2.extras import execute_values

# set file path
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.splite3")

# loaded into .env for security 
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

# connect with psycopg2
connection2 = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
cursor2 = connection2.cursor()

# ------------------------------------------------------
# ################## the hard way ######################

# converting the local csv to local db then adding to server

# connect to sqlite
connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

# read in csv and then append to db file 
labels = ['Survived','Pclass','Name','Sex','Age','Siblings_Spouses_Aboard','Parents/Children_Aboard','Fare']
df = pandas.read_csv('/home/terrence/Documents/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv',header=0, names=labels)
df.to_sql('titanic', con=connection, if_exists='append', index=False)


# read in db file
DB_path = "/home/terrence/Documents/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/titanic.sqlite3"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), DB_path)

query1 = 'SELECT * FROM titanic'
data = cursor.execute(query1).fetchall()

### iterate over the db and save tuples to list then push to server ###

# create table
new_table = """
CREATE TABLE IF NOT EXISTS titanic ( 
Survived INTEGER NOT NULL,
Pclass INTEGER NOT NULL,
Name VARCHAR(100),
Sex VARCHAR(7),
Age INTEGER NOT NULL,
Siblings_Spouses_Aboard INTEGER NOT NULL,
Parents_Children_Aboard INTEGER NOT NULL,
Fare DECIMAL (8,4)
);
"""
cursor2.execute(new_table)
connection2.commit()

my_list = []
for i in data:
    my_list.append(i)

insert_query = "INSERT INTO titanic (Survived,Pclass,Name,Sex,Age,Siblings_Spouses_Aboard,Parents_Children_Aboard,Fare) values %s"
execute_values(cursor2, insert_query, my_list)
connection2.commit()

# --------------------------------------------------
# ################## the easy way ##################

### create new table, open csv, skip the header, iter and insert 

new_table = """
CREATE TABLE IF NOT EXISTS titanic2 ( 
Survived INTEGER NOT NULL,
Pclass INTEGER NOT NULL,
Name VARCHAR(100),
Sex VARCHAR(7),
Age DECIMAL (5,1),
Siblings_Spouses_Aboard INTEGER NOT NULL,
Parents_Children_Aboard INTEGER NOT NULL,
Fare DECIMAL (8,4)
);
"""
cursor2.execute(new_table)
connection2.commit()

with open('/home/terrence/Documents/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cursor2.execute(
            "INSERT INTO titanic2 VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            row
        )
connection2.commit()

# ------------------------------------------------------

# always close at the end
if(connection2):
    cursor2.close()
    connection2.close()
    print("PostgreSQL connection is closed")

