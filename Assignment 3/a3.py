import sqlite3
conn = sqlite3.connect('./A3.db')
c = conn.cursor()
comm = 99

#Printing initial Display

print("Enter numbers from 1 to 5, to select an option..")
print("1. List the titles of accepted papers in a given area.")
print("2. Given a user's email, list only the titles of the papers he/she was assigned to review.")
print("3. Find papers with incosistent reviews, given the difference in percentage.")
print("4. Find papers according to difference score.")
print("5. Exit.")

#Incase DiffScore already exists, we will delete the existing view.
c.execute('''drop view if exists DiffScore;''')
conn.commit()

#Task 4, Creating a view called DiffScore
c.execute('''create view [DiffScore] as
        select p.id as pid, p.title as ptitle, ABS((SELECT AVG(reviews.overall) 
                                        FROM reviews
                                        WHERE reviews.paper = p.id) - 
                                        (select avg(reviews.overall) 
                                        from reviews, papers 
                                        where reviews.paper = papers.id 
                                        and papers.area = p.area)) as difference
        from papers as p, reviews
        group by p.id;''')
conn.commit()

#App runs as long as comm = 99, it is made sure that comm is rest after every task.
while(comm == 99):
    #Making sure that the selected option is valid.
    try:
        comm = int(input("Enter Option No. : "))
        assert (comm >= 1 and comm <= 5)
    except:
        print("Please enter a valid option")
        print('')
        comm = 99
    else:
        #Stop app if option selected is 5
        if (comm == 5):
            break

        #Task 1
        while(comm == 1):
            #Making sure that the entered Area name exists.
            try:
                y = input("Enter Area Name: ")
                c.execute('''select *
                            from areas
                            where ? = areas.name;''', (y,))
                rows = c.fetchall()
                assert len(rows) > 0
            except:
                print("This Area does not exist, please type a valid Area name")
            else:
                
                c.execute('''select papers.title
                            from reviews, papers 
                            where papers.area = ? and reviews.paper = papers.id and papers.decision = 'A'
                            group by papers.title
                            order by avg(reviews.overall) desc;''', (y,))
                conn.commit()
                rows = c.fetchall()
                print('')
                if(len(rows) == 0):
                    print("No such accepted papers were found")
                else:
                    print("Accepted papers in {0}: ".format(y))
                    for i in rows:
                        print(i[0])
                print('')
                comm = 99
        #Task 2
        while(comm == 2):
            #Making sure that entered Email exists
            try:
                y = input("Enter E-Mail: ")
                c.execute('''select *
                            from users
                            where ? = users.email;''', (y,))
                conn.commit()
                rows = c.fetchall()
                assert len(rows) > 0
            except:
                print("This E-Mail does not exist, please type a valid E-Mail")
                comm = 2
            else:
                    
                c.execute('''select papers.title
                            from reviews, papers 
                            where reviews.reviewer = ? and reviews.paper = papers.id
                            order by papers.id;''', (y,))
                conn.commit()
                rows = c.fetchall()
                
                #If rows is empty, it implies that no paper has been assigned to this reviewer.
                if len(rows) == 0:
                    print("No paper has been assigned to this reviewer ")
                else:
                    print("Papers reviewed by this reviewer: ")
                    print('')
                    for i in rows:
                        print(i[0])
                print('')
                comm = 99
        #Task 3
        while(comm == 3):
            #Making sure that the input is a positive number
            try:
                y = float(input("X = "))
                assert y > 0
            except:
                print("Please enter positive numbers for X")
                comm = 3
            else:           
                c.execute('''SELECT distinct p.id, p.title
                            from  papers p, reviews r
                            where r.paper = p.id and
                            ? < 100*ABS( 1 - r.overall/(
                            select AVG(r2.overall)
                            from reviews r2
                            where r2.paper = p.id));''', (y,))
                conn.commit()
                rows = c.fetchall()
                
                print('')
                if(len(rows) == 0):
                    print("No such papers were found")
                else:
                    print("Reviews inconsistent with {0}%:".format(y))
                    for i in rows:
                        print(i[0], i[1])
                print('')
                comm = 99
        #Task 4
        while(comm == 4):
            #Making sure that both x and y are positive numbers
            try:
                x = float(input("X = "))
                y = float(input("Y = "))
                assert x > 0 and y > 0
            except:
                print("Please enter positive numbers for X and Y")
                comm = 4
            else:
            
                c.execute('''SELECT reviews.reviewer, users.name
                            from reviews, users, DiffScore
                            where reviews.reviewer = users.email and DiffScore.difference >= ? 
                            and DiffScore.difference <= ? and reviews.paper = DiffScore.pid;''', (x,y,))
                conn.commit()
                rows = c.fetchall()
                print('')
                if(len(rows) == 0):
                    print("No such reviewers are found")
                else:
                    print("Reviews inconsistent in:", y)
                    for i in rows:
                        print(i[0], i[1])
                comm = 99
                print('')
