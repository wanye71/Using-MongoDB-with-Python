import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient

from bson.decimal128 import Decimal128

# Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' colleftion
accounts_collection = db.accounts

new_account = {
    "account_holder": "Kate Stone",
    "account_id": "MDB333829449",
    "account_type": "checking",
    "balance": Decimal128('4688'),
    'transfers_complete': [
        'TR854412948',
        'TR413308451',
        'TR328078274',
        'TR192714918',
        'TR263422717',
    ]
}

# Write an expression that inserts the 'new_account' document into the 'accounts' collection
result = accounts_collection.insert_one(new_account)

document_ids = result.inserted_id
# print("# of documents inserted: " + str(len(document_ids)))
print(f"_id of inserted document: {document_ids}")

client.close()