from pymongo import MongoClient
import csv
import time
client = MongoClient('mongodb://localhost:27012')

db = client["A5db"]
collection = db["listings"]
print(collection.count())
start_time = time.time()

result= collection.aggregate(
    [
    "reviews": {"$exists":False},
    {"$sort" : {"listing_id" : 1}},
    {"$limit" : 10}
    ])

print("Time take for completing query:", (time.time() - start_time)*1000, "ms")

print("Top 10 listing_ids with no reviews: (listing_id)")
for i in list(result)[:10]:
	print(i, "\n")