# Using Python with MongoDB
## MongoDB connection
```python
from  dotenv import load_dotenv
from pymongo import MongoClient

# Load config from .env file
load_dotenv()

MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)

for db_name in client.list_database_names():
    print(db_name)

client.close()
```
# MongoDB CRUD Operations in Python
## Working with MongoDB documents
```python
new_document = {
    "account_holder": "Addison Shelton",
    "account_id": "MDB955769550",
    "account_type": "checking",
    "years_active": 5,
    "address": {
        "city": "Ridgewook",
        "zip": "11385",
        "street": "Menahan St",
        "number": "1712",
    },
    "transfer_complete": [
        "TR28105502",
        "TR197586149",
        "TR586833243",
    ]
}
```
## Insert a single record
```python
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

new_account = {
    "account_holder": "Linus Torbalds",
    "account_id": "MDB829001337",
    "account_type": "checking",
    "balance": 50352434,
    "last_updated": datetime.datetime.utcnow()
}

# Write an expression that inserts the 'new_account' document into the 'accounts' collection
result = accounts_collection.insert_one(new_account)

document_ids = result.inserted_id
# print("# of documents inserted: " + str(len(document_ids)))
print(f"_id of inserted document: {document_ids}")

client.close()
```