import pymongo

client = pymongo.MongoClient("mongodb+srv://abhishek2296:mongodb@abhishek.5jqpvja.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Abhishek",
    "email" : "abc@cdf.com",
    "surname" : "rajput"
}
db1 = client["mongodb"]
coll = db1['test1']
coll.insert_one(d)

print("abcd")
