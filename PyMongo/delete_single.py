import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

# Import ObjuectId from bson package to enable querying by ObjectId
from bson.objectid import ObjectId

# Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connecct to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get referenc to 'accounts' collection
accounts_collection = db.accounts

# Filter by ObjectId
document_to_delte = {"_id": ObjectId("660ebf1ad1ad048cf377f4a6")}

# Search for document before delete
print("Searching for taget document before delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delte))

# Write an expression that deletes the tatget account.
result = accounts_collection.delete_one(document_to_delte)

# Search for documentt after delete
print("Searching for target document after delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delte))

print("Document(s) deleted: " + str(result.deleted_count))

client.close()