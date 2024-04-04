# Using Python with MongoDB
## Table of Contents
### CRUD
1. [Insert a Single Record ***CreateRUD***](#insert-a-single-record-createrud)
2. [Insert Multiple Records ***CreateRUD***](#insert-multiple-records-createrud)
3. [Find One Record ***CRreadUD***](#find-one-record-from-the-database-creadud)
4. [Find Multiple Records from the Database ***CRreadUD***](#find-multiple-records-from-the-database-creadud)
5. [Update a Single Document ***CRUpdateD***](#update-a-single-document-crupdated)
6. [Update Multiple Documents ***CRUpdateD***](#update-multiple-documents-crupdated)
7. [Delete Single Document ***CRUDelete***](#delete-single-document-crudelete)
8. [Delete Multiple Documents ***CRUDelete***](#delete-multiple-documents-crudelete)
### Transactions
9. [Creating Transactions](#creating-transactions)
### Aggregation
10. [Match and Grouping](#match-and-grouping)

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
## Insert a single record ***CreateRUD***
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

## Insert multiple records ***CreateRUD***
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
```

## Find One Record from the Database ***CReadUD***
```python
import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

# Import ObjectId from bson package (part of PyMongo distibution) to enable querying by ObjectId
from bson.objectid import ObjectId

# Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get referenct to the 'accounts' collection
accounts_collection = db.accounts

# Query by ObjectId
document_to_find = {"_id": ObjectId("660e64c8c9ed0ca427e158ff")}

# Write an expression that retrieves the document matching the query constraint (i.e. find_one) in the 'accounts' collection.
result = accounts_collection.find_one(document_to_find)
pprint.pprint(result)

client.close()
```

## Find Multiple Records from the Database ***CReadUD***
```python
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
```
## Update a single document ***CRUpdateD***
```python
# Python scripts to interact with the operating system. 
import os
# provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter
import pprint

# loads environment variables from a .env
import dotenv as load_dotenv
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
```
## Update Multiple Documents ***CRUpdateD***
```python
import os

import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Filter
select_accounts = {"account_type": "Savings"}

# Update
set_field = [
    {"$set": {"earned_interest": 500}},
    {"$set": {"transfers_completed": []}},
]

# Write an expression that adds a minimum balance field to each savings document and sets the value to 100
result = accounts_collection.update_many(select_accounts, set_field)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint.pprint(accounts_collection.find_one(select_accounts))

client.close()
```
## Delete Single Document ***CRUDelete***
```python
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
```

## Delete Multiple Documents ***CRUDelete***
```python
import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get reference to the 'accounts' collection
accounts_collection = db.accounts

# Filter for accounts with balance less than $2000
documents_to_delete = {"balance": {"$lt": 7000}}

# Search for sample document before delete
print("Searching for sample target document before delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

# Write an expression that deletes the target accounts.
result = accounts_collection.delete_many(documents_to_delete)

print("Searching for sample target document after delete:")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

print("Documents deleted: " + str(result.deleted_count))

client.close()
```
# Transactions
## Creating Transactions
```python
import os

from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Step 1: Define the callback that specifies the sequence of operations to perform inside the transaction
def callback(session,transfer_id=None, account_id_receiver=None, account_id_sender=None,transfer_amount=None):
        # Get reference to 'accounts' collection
        accounts_collection = session.client.bank.accounts

        # Get reference to 'transfers' collection
        transfers_collection = session.client.bank.transfers

        transfer = {
            "transfer_id":transfer_id,
            "to_account": account_id_receiver,
            "from_account": account_id_sender,
            "amount": {"$numberDecimal": transfer_amount}
        }

        # Transaction operations
        # Important: You mist pass the session to each operation
        # Update sender amount: subtract transfer amount from balance and add transfer ID
        accounts_collection.update_one(
                {"account_id": account_id_sender},
                {
                    "$inc": {"balance": transfer_amount},
                    "$push": {"transfers_complete": transfer_id}
                },
                session=session
        )

        # Add new transfer to 'transfers' collection
        transfers_collection.insert_one(transfer, session=session)

        print("Transaction successful")

        return

def callback_wrapper(s):
        callback(
                s,
                transfer_id="TR218721873",
                account_id_receiver="MDB343652528",
                account_id_sender="MDB574189300",
                transfer_amount=100
        )
# Start a client session, then start a transaction.
with client.start_session() as session:
        session.with_transaction(callback_wrapper)
    
client.close()
```
# Aggregation
## Match and Grouping
```python
import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank 

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Calculate the average balance of checking and savings accounts with balances of less than $10000.

# Select accounts with balances of less than $10000.
select_by_balance = {"$match": {"balance": {"$lt": 10000}}}

# Separate documents by account tupe and calculate the average balance for each account type.
separate_by_account_calculate_avg_balance = {
    "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
}

# Create an aggregation pipeline using 'stage_match_balance' and 'stage_group_account_type'.
pipeline = [
    select_by_balance,
    separate_by_account_calculate_avg_balance
]

# Perform an aggregation on 'pipeline'
results = accounts_collection.aggregate(pipeline)

print()
print(
    "Average balance of checking and savings accounts with balance of less than $10000"
)

for item in results:
    pprint.pprint(item)

client.close()
```