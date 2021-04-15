import sqlite3
import csv
import time

print("Executing Part 2\n\n")

databases = ['./A4v100.db', './A4v1k.db', './A4v10k.db','./A4v100k.db','./A4v1M.db']

print("Executing Task 6\n")
for base in databases:
	print("Opening", base[2:])
	conn = sqlite3.connect(base)
	c = conn.cursor()
	
	print("Running Query")

	start_time = time.time()
	for i in range (0, 100):
		c.execute('''select avg(parts.partPrice) from Parts group by parts.madein''')
		conn.commit()
	print("Average query time for Query Q3: {0} ms \n".format((time.time() - start_time)*1000/100))

print("Creating Index\n")
for base in databases:
	conn = sqlite3.connect(base)
	c = conn.cursor()
	c.execute('''CREATE INDEX idxMadeIn ON Parts ( MadeIn );''')
	conn.commit()

print("Executing Task 7")
for base in databases:
	print("Opening", base[2:])
	conn = sqlite3.connect(base)
	c = conn.cursor()
	
	print("Running Query")

	start_time = time.time()
	for i in range (0, 100):
		c.execute('''select avg(parts.partPrice) from Parts group by parts.madein''')
		conn.commit()
	print("Average query time for Query Q3 with index: {0} ms \n".format((time.time() - start_time)*1000/100))
