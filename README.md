# Python-Final
Python FInal
by Jack Gann
The libraries I will be using for this project is Tkinter and Sqlite3.
My program will utilize Tkinter and Sqlite3 to create a database and use it as a grocery list. I will use Tkinter to create a user-friendly GUI where they will be able to input information that will be added to the database using Sqlite3. 
On the GUI there will be multiple buttons that will not only allow the user to submit information into the database but also write the information into a file for the user to look over. The format the user will input information is: (what item needed from the grocery store), (quantity needed). 
Inside the code I will be using multiple methods from Tkinter such as: Label, Button, bind, mainloop, title.
I will be using methods from sqlite3 such as: execute, cursor, connect.
Inside the code I will use various methods to make sure no user error can occur. The program will prompt the user for the input and send it over to a method. There the method will split the string into two strings and check to see if the item has already been added the the database. If so then the program will update the QTY of said item. If the user wants the program to output the information to a text file then the program will use a method that will traverse through the database and write to a text file outside of the program. 
The database will have one table called Items. The table will have 2 columns: Item | QTY.


```python
# Import required Libraries.
import tkinter
import sqlite3

# Initialize database. If it exists then we just add up all the items to be displayed on the GUI
dataCounter = 0
try:
    initalize database("grocery.sqlite")
except:
    for i in database:
        dataCounter++

# Method to add the item into the database
def addItem(*args):
    # If the table already exists then we just add the information. If it doesn't we create the table.
    try:
        database.execute(CREATE TABLE)
    except:
        pass
    # Check if the item is in the table. If it is update the quantity. 
    if item is in table:
        database.execute(UPDATE QTY)
    else:
        convert string into lowercase
        separate string into two strings
        database.execute(insert data into rows)
        dataCounter++
# Method to export the information into a text file.
def export(*args):
    for i in database:
        file.write(i)
# Method to delete the items inside the database. 
def deleteItems():
    database.execute(DROP TABLE)
    close()


# Initalize the GUI
kin.title("Grocery List")
initialize mainframe
initialize button("Submit", command=addItem)
initialize button("Export", command=export)
initialize button("Close/Clear Database", command=deleteItems)
    


# Start the main loop of the program. 
kin.mainloop()
```