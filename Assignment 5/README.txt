NAMES: Raj Shreyas Penukonda, Jaspreet Kaur Sohal
CCIDs: penukond, jsohal
Student IDs: 1623713, 1620817

This assignment was done together by the names mentioned above.

Included files:

-A5T1.py
-A5T2.py

-A5T3SQLite.py
-A5T4SQLite.py
-A5T6SQLite.py
-A5T8SQLite.py

-A5T3MongoDB.py
-A5T4MongoDB.py
-A5T6MongoDB.py
-A5T8MongoDB.py
-A5T9MongoDB.py

We completed tasks 3, 4, 6, 8, 9

How to run SQL applications:
1. Make sure all the files above are in the same directory
2. Create the SQLite database by type this in the terminal: python3 A5T1.py
3. Create the MongoDB database by type this in the terminal: python3 A5T2.py


How to execute the tasks:

To run any of the SQLite tasks type the following and replace x with the task number: python3 A5TxSQLite.py
To run any of the MongoDB tasks type the following and replace x with the task number: python3 A5TxMongoDB.py

Tasks 3 and 4 will show the output after typing their respective terminal commands

Task 6:

Type the name of the neighbourhood of which the prices should be increased when prompted for it.
It is assumed that the user types a neighbourhood that exists. If not, there will be no updates made.

Example Execution:
---------------------------------------------------------------
>>>python3 A5T6SQLite.py
Enter the name of neighbourhood to increase its prices: Downtown
Time taking for updating: 217.2703742980957 ms
Prices of all listings in Downtown increased by 10%
---------------------------------------------------------------

Task 8:

Type the listing_id of which the review should be shown when prompted
The app will show an error asking for a valid id if the the input is not a positive intger

Example Execution:
---------------------------------------------------------------
>>>python3 A5T8SQLite.py
Enter a listing_id to get the most recent review for: 226757
Time taken for completing the query: 1077.1949291229248 ms

Result of the query: (Host name, price, most recent comment)

('Vancouver Furnished', 153.73, 'Me gusto mucho la ubicación del lugar y lo acogedor que es lo recomiendo mucho')
---------------------------------------------------------------
