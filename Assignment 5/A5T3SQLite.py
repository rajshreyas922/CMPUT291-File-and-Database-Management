import sqlite3
import csv
import time

def main():
	conn = sqlite3.connect("A5.db")
	c = conn.cursor()
	#Query in sql to get the required output
	start_time = time.time()
	c.execute('''select count(*), listings.host_id
				from listings
				group by listings.host_id
				order by listings.host_id;''')
	print("Time taken for query:", (time.time() - start_time)*1000, "ms")

	#print top 10
	print("Top 10 results: (Number of listings, host_id)")
	rows = c.fetchall()
	for i in rows[0:10]:
		print(i)


#call main function
if __name__ == "__main__":
	main()