from pymongo import MongoClient
import csv
import time

client = MongoClient('mongodb://localhost:27012')

db = client["A5db"]
collection = db["listings"]

start_time = time.time() #Start recording time
keywords=input("enter: ").split(", ")
for each_keyword in keywords:
    split "comments" based on " " (so we have each word)
result = collection.find( { qty: { $in: splitVersionOfComment} } ).sort(basedOnMostSimilarSomehow)

print("\nTime taken for query:", (time.time() - start_time)*1000, "ms")

print("The top 3 listings are: ",result[0], result[1], result[2])