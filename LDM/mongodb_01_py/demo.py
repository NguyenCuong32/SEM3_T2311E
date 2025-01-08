from pymongo import MongoClient



connection_string = "mongodb://root:123456@127.0.0.1:27017/"

client = MongoClient(connection_string)

db = client["DemoDB"]
collections = db["Users"]
if collections is not None:
    document = collections.find()
    print("Connected")
    for doc in document:
        print(doc["username"])
        print(doc["fullname"])
else:
    print("Can not connected")


