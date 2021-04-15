from pymongo import MongoClient
import csv
import time

client = MongoClient('mongodb://localhost:27012')

db = client["A5db"]
collection = db["listings"]

start_time = time.time() #Start recording time
result = collection.aggregate([
  {"$group": {"_id": "$host_id", "count": {"$sum": 1}}}, {"$sort" : {"host_id":1}}, {"$limit" : 10}
])
print("\nTime taken for query:", (time.time() - start_time)*1000, "ms")

print("Top 10 results: (Number of listings, host_id)")
for i in list(result):
	print(i, "\n")