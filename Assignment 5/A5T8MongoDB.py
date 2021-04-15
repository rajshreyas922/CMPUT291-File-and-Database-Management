from pymongo import MongoClient
import csv
import time

client = MongoClient('mongodb://localhost:27012')

db = client["A5db"]
collection = db["listings"]

start_time = time.time() #Start recording time
list_id = input("input: ")
result = collection.find({"listing_id":list_id},{"host_name":1, "rental_price":1} ).sort("date")
print("\nTime taken for query:", (time.time() - start_time)*1000, "ms")

print("Most recent review for this listing: ",result[0])