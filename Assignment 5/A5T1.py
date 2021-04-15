import sqlite3
import csv

def insertValuesListings():
	try:
		conn = sqlite3.connect("A5.db")
		c = conn.cursor()
		c.execute('''DROP TABLE listings;''')
		conn.commit()
	except:
		pass

	conn = sqlite3.connect("A5.db")
	c = conn.cursor()

	with open('YVR_Airbnb_listings_summary.csv', 'r') as csvfile:
		read=csv.reader(csvfile, delimiter=',')
		listings = list(read)

	c.execute('''create table listings(id,name,host_id,host_name,neighbourhood,room_type,price,minimum_nights,availability_365, 
				PRIMARY KEY (id));''')
	conn.commit()

	print("Inserting values into listings...")
	for i in listings[1:]:
		c.execute('''INSERT INTO listings(id,name,host_id,host_name,neighbourhood,room_type,price,minimum_nights,availability_365)
						VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
						''', (int(i[0]), (i[1]), int(i[2]), (i[3]), i[4], i[5], float(i[6]), int(i[7]), int(i[8]),))
		conn.commit()
	print("Done\n")

def insertValuesReviews():
	try:
		conn = sqlite3.connect("A5.db")
		c = conn.cursor()
		c.execute('''DROP TABLE reviews;''')
		conn.commit()
	except:
		pass
	conn = sqlite3.connect("A5.db")
	c = conn.cursor()
	with open('YVR_Airbnb_reviews.csv', 'r') as csvfile:
		read=csv.reader(csvfile, delimiter=',')
		reviews = list(read)

	c.execute('''create table reviews(listing_id, id, date, reviewer_id, reviewer_name, comments,
				PRIMARY KEY (id),
				FOREIGN KEY (listing_id) REFERENCES listings(id));''')
	conn.commit()

	print("Inserting values into reviews...")
	for i in reviews[1:]:
		c.execute('''INSERT INTO reviews(listing_id, id, date, reviewer_id, reviewer_name, comments)
						VALUES(?, ?, ?, ?, ?, ?);''', (int(i[0]), int(i[1]), i[2], int(i[3]), i[4], i[5],))
		conn.commit()

	print("Done\n")


def main():
	insertValuesListings()
	insertValuesReviews()

#call main function
if __name__ == "__main__":
	main()