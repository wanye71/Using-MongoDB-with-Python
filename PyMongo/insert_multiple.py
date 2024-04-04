import datetime
import os
import json

from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' colleftion
accounts_collection = db.accounts

# Read the contents of the JSON file
with open('bank_customer.json', 'r') as file:
    json_data = json.load(file)

new_accounts = list(json_data)

# Write an expression that inserts the 'new_account' document into the 'accounts' collection
result = accounts_collection.insert_many(new_accounts)

document_ids = result.inserted_ids
print("# of documents inserted: " + str(len(document_ids)))
print(f"_id of inserted document: {document_ids}")

client.close()