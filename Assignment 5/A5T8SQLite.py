import sqlite3
import time
import csv

def main():
	conn = sqlite3.connect("A5.db")
	c = conn.cursor()
	
	bool = True
	while(bool):
		try:
			l_id = int(input("Enter a listing_id to get the most recent review for: ")) #Taking input for the listing_id as an integer
			assert l_id > 0
			bool = False
		except:
			print("Enter a valid id (Positive integer) \n")

	start_time = time.time() #Start counting time

	#SQL Query to get most host name, price, and recent review of the given listing_id
	c.execute('''select listings.host_name, listings.price, reviews.comments
				from listings, reviews
				where listings.id = ? and reviews.listing_id = ? 
				and date(reviews.date) = (select max(date(reviews.date)) from reviews where reviews.listing_id = ?);''', (l_id, l_id, l_id,))
	print("Time taken for completing the query:", (time.time() - start_time) * 1000, "ms")

	print("\n"+"Result of the query: (Host name, price, most recent comment)\n")
	#Print the result of query

	rows = c.fetchall()
	if(len(rows) == 0):
		print("No review found")
	else:
		print(rows[0])
	print("")

#call main function
if __name__ == "__main__":
	main()