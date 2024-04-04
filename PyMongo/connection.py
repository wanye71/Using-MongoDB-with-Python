from pymongo import MongoClient

MONGO_URI = "mongodb+srv://techwithwayne:Tylerhaller!23@cluster0.kswvxmx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)

for db_name in client.list_database_names():
    print(db_name)