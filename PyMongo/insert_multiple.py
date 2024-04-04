import datetime
import os

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

new_accounts = [
    {
        "account_id": "MB011235813",
        "account_holder": "Ada Lovelace",
        "account_type": "checking",
        "balance": 60218,
    },
    {
        "account_id": "MDB829000001",
        "account_holder": "Muhammad ibn Musa al-Khwarizmi",
        "account_type": "checking",
        "balance": 267914296,
    },
]

# Write an expression that inserts the 'new_account' document into the 'accounts' collection
result = accounts_collection.insert_many(new_accounts)

document_ids = result.inserted_id
print("# of documents inserted: " + str(len(document_ids)))
print(f"_id of inserted document: {document_ids}")

client.close()