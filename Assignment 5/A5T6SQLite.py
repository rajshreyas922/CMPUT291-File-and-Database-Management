import sqlite3
import time
import csv


def main():
	conn = sqlite3.connect("A5.db")
	c = conn.cursor()

	n = (input("Enter the name of neighbourhood to increase its prices: ")) #Taking input as string
	start_time = time.time()
	#SQL Query to increase the prices by 10%
	c.execute('''update listings
	 			set price = round(1.1 * price, 2)
				where ? = neighbourhood;''', (n,))
	print("Time taking for updating:", (time.time() - start_time) * 1000, "ms")
	
	print("Prices of all listings in "+n+" increased by 10%")
	conn.commit()

#call main function
if __name__ == "__main__":
	main()