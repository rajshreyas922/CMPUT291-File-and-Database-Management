from pymongo import MongoClient
import csv

client = MongoClient('mongodb://localhost:27012')

db = client["A5db"]
collection = db["listings"]
print(collection.count())
n = input("Enter neighbouthood: ")
#db.collection.update(
 # {"neighbourhood":n},
  #{ $set: { "price": { $eq: 1.1*"price" } } },
 # { multi: true }
#)
n = input("in: ")
result = db.collection.update(
  {"neighbourhood" : { "$eq": n}},
 { "$mul": { "price": 1.1 } },
  { "multi": True }
)

for i in list(result)[:10]:
	print(i, "\n")

