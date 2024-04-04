# Python scripts to interact with the operating system. 
import os
# provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter
import pprint

# loads environment variables from a .env
from dotenv import load_dotenv
# Connect to and interact with a MongoDB database.
from pymongo import MongoClient

# Import ObjectId from bson package to enable querying by ObjectId
from bson.objectid import ObjectId

# Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# filter
document_to_update = {"_id": ObjectId("660ebf1ad1ad048cf377f4a6")}

# Update
add_to_balance = {"$inc": {"balance": 100}}

# Print original document
pprint.pprint(accounts_collection.find_one(document_to_update))

# Write expression that adds to the target account balance by the specified amount.
result = accounts_collection.update_one(document_to_update, add_to_balance)
# Print the number of documents modified
pprint.pprint("Documents updated: " + str(result.modified_count))

# Print updated document
pprint.pprint(accounts_collection.find_one(document_to_update))

client.close()