import pandas
import sqlite3
import os

# file path
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.splite3")

# connection
connection = sqlite3.connect(DB_FILEPATH)

# loading in csv
labels = ['user_id','sports','religious','nature','theatre','shopping','picnic']

# had to remove header then add column names with no spaces and lowecase for ease of acces
# labels with white speces give error in sql query
df = pandas.read_csv('/home/terrence/Documents/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv',header=0, names=labels)
df.to_sql('Buddy_works', con=connection, if_exists='append', index=False)

# queries
query = 'SELECT COUNT(DISTINCT user_id) AS count FROM Buddy_works'
query2 = 'SELECT COUNT(DISTINCT user_id) FROM Buddy_works WHERE nature >=100 AND shopping >= 100'
query3 = 'SELECT AVG(nature) FROM Buddy_works'

# cursor
cursor = connection.cursor()

# Q1
result = cursor.execute(query).fetchall()
print('Total rows:',result)

# Q2
result = cursor.execute(query2).fetchall()
print('Nature and Shopping >= 100:', result)

# Q3
result = cursor.execute(query3).fetchall()
print('Average Nature', result)

# geting the average of all columns in table 
my_list = ['sports','religious','nature','theatre','shopping','picnic']
for i in my_list:
    query = f'SELECT AVG({i}) FROM Buddy_works'
    result = cursor.execute(query).fetchall()
    print(f'Average Number of Reviews For {i}:',result)

# pandas function to run sql in one line
df2 = pandas.read_sql(query, connection)
print(df2)
