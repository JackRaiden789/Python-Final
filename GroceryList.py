# Import required Libraries.
from tkinter import *
from tkinter import ttk
import sqlite3

# Initialize database. I
dataCounter = 0
conn = sqlite3.connect('grocery.sqlite')
cur = conn.cursor()
for i in database:
    dataCounter++

# Method to add the item into the database
def addItem(*args):
    unSplitstring = userEntry.get()
    # If the table already exists then we just add the information. If it doesn't we create the table.
    try:
        database.execute(CREATE TABLE)
    except:
        pass
    # Check if the item is in the table. If it is update the quantity. 
    unSplitstring = unSplitstring.lower()
    splitstring = unSplitstring.split(", ")
    item = splitstring[0]
    qty = splitstring[1]
    if item is in table:
        database.execute(UPDATE QTY)
    else:
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
