import sqlite3
import time
import csv

def main():
	conn = sqlite3.connect("A5.db")
	c = conn.cursor()

	start_time = time.time()
	#Query to find which listings have not recieved any review
	c.execute('''select (listings.id)
				from listings
				where listings.id not in (select L.id from listings L, reviews where L.id = reviews.listing_id)
				group by listings.id
				order by listings.id;''')
	print("Time take for completing query:", (time.time() - start_time)*1000, "ms")

	#print required output
	print("Top 10 listing_ids with no reviews: (listing_id)")
	rows = c.fetchall()
	for i in rows[0:10]:
		print(i)


#call main function
if __name__ == "__main__":
	main()