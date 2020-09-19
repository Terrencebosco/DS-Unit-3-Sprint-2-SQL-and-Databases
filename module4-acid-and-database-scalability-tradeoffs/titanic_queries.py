import json
import sqlite3
import os
import psycopg2
import pandas
import csv
from dotenv import load_dotenv
from psycopg2.extras import execute_values

# loaded into .env for security 
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
cursor = connection.cursor()

# number survived 545
query1 = """ 
SELECT count(*) FROM titanic
WHERE Survived = 0
"""
# class 1 216
query2 = """ 
SELECT COUNT(*) FROM titanic
WHERE pclass = 1
"""
# class 2 184
query3 =""" 
SELECT COUNT(*) FROM titanic
WHERE pclass = 2
"""
# class 3 487
query4 =""" 
SELECT COUNT(*) FROM titanic
WHERE pclass = 3
"""

# number of each class that died
for i in [1, 2, 3]:
    query = f"""
    SELECT COUNT(*) FROM titanic
    WHERE pclass = {i} AND Survived = 0
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print(f"for pclass {i}, {result} died.")
print("---")

# number of each classed that survived
for i in [1, 2, 3]:
    query = f"""
    SELECT COUNT(*) FROM titanic
    WHERE pclass = {i} AND Survived = 1
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print(f"for pclass {i}, {result} survived.")
print("---")

# average age of survived
query5 = """
SELECT AVG(age) FROM titanic
WHERE survived = 1
"""
# average age of died
query6= """
SELECT AVG(age) FROM titanic
WHERE survived = 0
"""
# average age of survived
query7 = """
SELECT AVG(age) FROM titanic
WHERE survived = 1
"""

# average fare for each class
for i in [1,2,3]:
    query = f"""
    SELECT AVG(fare) FROM titanic 
    WHERE pclass = {i}
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print(f"for pclass {i}, the average fare is {result}")

# average sibling, spouse for each class
for i in [1,2,3]:
    query = f"""
    SELECT AVG(siblings_spouses_aboard) FROM titanic 
    WHERE pclass = {i}
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print(f"for pclass {i}, the average siblings and spouses: {result}")
print("---")

# average parants children aboard
for i in [1,2,3]:
    query = f"""
    SELECT AVG(parents_children_aboard) FROM titanic 
    WHERE pclass = {i}
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print(f"for pclass {i}, the average parents and children: {result}")

def run_query(query):
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    connection.close()

run_query(query)

if(connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")