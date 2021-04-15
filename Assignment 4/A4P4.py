import sqlite3
import csv
import random
import time

conn= None
c= None

def dropIndex():
	c.execute('''
			  DROP INDEX idxNeedsPart;
			  ''')
	conn.commit()
	return

# This function connects the database to our python program
def connect(path):
	global conn, c
	conn = sqlite3.connect(path)
	c = conn.cursor()
	c.execute(' PRAGMA foreign_keys=ON; ')
	print(path[2:])
	conn.commit()
	return

def task13():
	print("Running Query")
	start_time = time.time()
	for i in range (0, 100):
		c.execute(''' select count(parts.partNumber)
					  from Parts
					  where not exists (select p.partNumber from Parts p where p.partNumber = parts.needsPart);
					  ''')
		conn.commit()
	print("Average query time for Query Q5 {0} ms\n".format(str((time.time() - start_time)*10)))

def task14():
	print("Running Query")
	start_time = time.time()
	for i in range (0, 100):
		c.execute('''  select count(p.partnumber)
					  from Parts p
					  where p.partNumber NOT IN (select parts.needsPart from Parts)
					 ''')
	print("Average query time for Query Q6 {0} ms\n".format(str((time.time() - start_time)*10)))
	conn.commit()
	print("----------------------------------------")

def main():
	global conn, c
	print("Executing Part 4\n")
	databases = ['./A4v100.db', './A4v1k.db','./A4v10k.db','./A4v100k.db','./A4v1M.db']

	print("Executing Task 13\n")
	for path in databases:
		print("Opening", path[2:])
		connect(path) #connect path to the database0
		task13()

	print("----------------------------------------")

	print("Executing Task 14\n")
	for path in databases:
		print("Opening", path[2:])
		connect(path) #connect path to the database0
		task14()

	print("----------------------------------------")
	

	print("Dropping index idxMadeIn\n")
	for path in databases:
		connect(path) #connect path to the database
		try:
			dropIndex()
		except:
			pass

	print("Creating indices for all the databases")
	for path in databases:
		connect(path)
		c.execute('''create index idxNeedsPart on parts(needspart)''')

	print("Executing Task 17\n")
	for path in databases:
		print("Opening", path[2:])
		connect(path) #connect path to the database0
		task14() #Calling task14 but it is running with indexes created which is task 17. 
	print("----------------------------------------")

	return

#call main function
if __name__ == "__main__":
	main()