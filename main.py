import json

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['gis']
collection = db['gis']

# Insert GeoJSON data in smaller chunks
with open('data/Tuman_27_03_2024.geojson', 'r', encoding='utf-8') as f:
    geojson_data = json.load(f)


# Define a function to split the GeoJSON features into chunks
def chunk_features(features, chunk_size):
    for i in range(0, len(features), chunk_size):
        yield features[i:i + chunk_size]


# Split the features into chunks and insert each chunk separately
chunk_size = 1000  # Adjust the chunk size as needed
for chunk in chunk_features(geojson_data['features'], chunk_size):
    collection.insert_many(chunk)
