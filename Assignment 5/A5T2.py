from pymongo import MongoClient
import csv

client = MongoClient('mongodb://localhost:27012')

db = client["A5db"]
collection = db["listings"]
#print(client.list_database_names())  


with open('YVR_Airbnb_reviews.csv', 'r') as csvfile:
	read=csv.reader(csvfile, delimiter=',')
	reviews = list(read)

#all info about reviews		
review_list=[]
review_dict={}

for a in range(1, len(reviews)):

	review_dict[reviews[0][0]]=int(reviews[a][0])
	review_dict[reviews[0][1]]=int(reviews[a][1])
	review_dict[reviews[0][2]]=reviews[a][2]
	review_dict[reviews[0][3]]=int(reviews[a][3])
	review_dict[reviews[0][4]]=reviews[a][4]
	review_dict[reviews[0][5]]=reviews[a][5]
	review_list.append(review_dict.copy())

for i in review_list[0:10]:
	print((i), "\n")

			
with open('YVR_Airbnb_listings_summary.csv', 'r') as csvfile:
		read=csv.reader(csvfile, delimiter=',')
		listings = list(read)
		
#all info about listing
temp = collection.delete_many({})
mylist=[]
mydict={"reviews":[]}
r_list=[]


print("Inserting values to listings collection")
for i in range(1,len(listings)):
	
	mydict[listings[0][0]]=int(listings[i][0])
	mydict[listings[0][1]]=listings[i][1]
	mydict[listings[0][2]]=int(listings[i][2])
	mydict[listings[0][3]]=listings[i][3]
	mydict[listings[0][4]]=listings[i][4]
	mydict[listings[0][5]]=listings[i][5]
	mydict[listings[0][6]]=float(listings[i][6])
	mydict[listings[0][7]]=int(listings[i][7])
	mydict[listings[0][8]]=int(listings[i][8])

	for each in review_list:
		if(each["listing_id"] == int(listings[i][0])):
			mydict["reviews"].append(each.copy())
			review_list.remove(each)

	mylist.append(mydict.copy())

collection.insert_many(mylist)
print(collection.count())
