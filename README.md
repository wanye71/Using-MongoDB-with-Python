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