from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Select the database
db = client['app']

# Select the collection
collection = db['regions1']

# Data to be inserted
try:
    with open("data/regions_2.json", "r") as file:
        data = json.load(file)
    # Insert data
    collection.insert_many(data)
    print("Data inserted successfully")
except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

