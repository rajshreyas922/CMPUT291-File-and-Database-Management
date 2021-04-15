import sqlite3
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

def dropIndex():
    c.execute('''
              DROP INDEX idxMadeIn;
              ''')
    conn.commit()
    return

def createIndex():
    c.execute('''create index idxMadeIn_idxPartPrice on Parts(madeIn, partPrice);''')
    return

def task3():
        start_time = time.time()
        for i in range (0, 100):
            c.execute('''    select madein from Parts  
                    order by random()
                    limit 1;''')
            rows = c.fetchall()
            for i in rows:
                rand_country = i[0]
            
            c.execute('''select max(Parts.partPrice)
                    from Parts
                    where Parts.madein = ?;''',(rand_country,))
            conn.commit()
        print("Average query time for Query 4 {}".format((time.time() - start_time)*1000/100))

        conn.commit()
        return
    
def main():
    global conn, c
    print("Executing Part 3\n")
    databases = ['./A4v100.db', './A4v1k.db', './A4v10k.db','./A4v100k.db','./A4v1M.db']
    print("Dropping index idxMadeIn\n")
    for path in databases:
        connect(path) #connect path to the database
        try:
            dropIndex()
        except:
            pass
    for path in databases:
        connect(path) #connect path to the database
        print("Opening {} ".format(path[2:]))
        task3()
        print("Closing {} ".format(path[2:]))
        print("-----------------------------------------------------\n")
    print("Creating index\n")
    for path in databases:
        connect(path) #connect path to the database
        c.execute('''create index idxMadeIn_idxPartPrice on Parts(madeIn, partPrice);''')
        print("Opening {} ".format(path[2:]))
        task3()
        print("Closing {} ".format(path[2:]))
        print("-----------------------------------------------------\n")
    conn.commit()

    return

#call main function
if __name__ == "__main__":
    main()
