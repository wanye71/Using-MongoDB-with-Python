import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

# Import ObjectIds from bson package to enable querying by ObjectId
from bson import ObjectId

# Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Query
# Find all accounts that have a balance greater than $4,700
documents_to_find = {"balance": {"$gt": 4700}}

# Write the expression that selects the documents matching the query constraint in the 'accounts' collection.
cursor = accounts_collection.find(documents_to_find)

num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()
    print("----------- New Record -------------")
    print()
print("# of docuemts found: " + str(num_docs))

client.close()