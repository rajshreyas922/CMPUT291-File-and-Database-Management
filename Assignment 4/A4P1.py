import sqlite3
import random
import time

conn= None
c= None

# This function connects the database to our python program
def connect(path):
    global conn, c
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute(' PRAGMA foreign_keys=ON; ')
    conn.commit()
    return

def createIndex():
    c.execute('''
              CREATE INDEX idxNeedsPart ON Parts ( needsPart );
             ''')
    return
              
def task1():
    run=0
    time_start = time.time()
    while run<100:
        c.execute('''
                  SELECT partNumber FROM Parts;
                  ''')
        partNumbers = c.fetchall()
        i=0
        for numbers in partNumbers:
            partNumbers[i]=numbers[0]
            i+=1
        U = random.choice(partNumbers)
    
        c.execute('''
                       SELECT partPrice FROM Parts
                       WHERE partNumber = ?
                       ''',(U,))
        run += 1
    part_time = time.time() - time_start

    time_start = time.time()
    run=0
    while run<100:
        c.execute('''
                  SELECT needsPart FROM Parts;
                  ''')
        needsParts = c.fetchall()
        i=0
        for numbers in needsParts:
            needsParts[i]=numbers[0]
            i+=1
        U = random.choice(needsParts)
    
        c.execute('''
                       SELECT partPrice FROM Parts
                       WHERE needsPart = ?
                       ''',(U,))
        
        run+=1
    need_time = time.time() - time_start

    print("Average query time for Query Q1: {} ms".format(need_time*1000/100) )
    print("Average query time for Query Q2: {} ms".format(part_time*1000/100) )

    
 
       
            
def main():
    global conn, c
    print("Executing Part 1")
    print("Executing Task A")
    databases = ['./A4v100.db', './A4v1k.db', './A4v10k.db','./A4v100k.db','./A4v1M.db']
    for path in databases:
        connect(path) #connect path to the database
        print("Opening {} ".format(path[2:]))
        task1()
        print("Closing {} ".format(path[2:]))
        print("-----------------------------------------------------")
    print("Creating Index")
    for path in databases:
        connect(path) 
        createIndex()
    print("Executing Task C")
    for path in databases:
        connect(path) #connect path to the database
        print("Opening {} ".format(path[2:]))
        task1()
        print("Closing {} ".format(path[2:]))
        print("-----------------------------------------------------")
    return

#call main function
if __name__ == "__main__":
    main()
