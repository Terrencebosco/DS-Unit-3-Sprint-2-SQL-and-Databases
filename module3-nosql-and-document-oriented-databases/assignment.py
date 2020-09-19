import pymongo
import os
from dotenv import load_dotenv
import sqlite3
import numpy as np

# gather data to push to mongoDB
DB_path = '/home/terrence/Documents/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3'
DB_FILEPATH = os.path.join(os.path.dirname(__file__), DB_path)

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION",connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query_to_pull_data = "SELECT * FROM charactercreator_character"
data = cursor.execute(query_to_pull_data).fetchall()

# getting character id and name from the list of tuples
data = np.array(data)
char_id = data[:,0]
char_names = data[:,1]
# -----------------------------------------------------------

# connect to mongoDB
DB_USER = os.getenv("MONGO_USER", default="OOOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)

# make new database
db = client.rpg_db
print(type(db))

collection = db.charactercreators

#breakpoint()

# add char id
for i in char_id:
    collection.insert_one({
        "character_id":str(i)
    })

# add char name
for i in char_names:
    collection.insert_one({
        "character_name":str(i)
    })

print(collection.count_documents({}))
# for doc in collection.find('character_id':{'$gt':100}):
#     print(doc)