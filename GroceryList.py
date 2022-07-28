''' 
My program creates a grocery list using sqlite as a database and exporting
it to a file. I tested my program first by making sure that the program will write
to a database file. Opening it and inputing test data such as: eggs| 1. This was 
successful at first until I realized that when I closed the program the items inside
the database were being deleted. I had to close the database and make sure that when 
I connected to it that it would connect locally. For example using the (./) specifying 
that it is on the local disk. I tested to make sure that the program could handle most 
user inputs and output an error depending on the input the user gave. If you try to 
input a number instead of a text into the item name. It will output that there is an
error in the user inputs. Same goes for when you put a text into the qty area instead 
of a number. I wanted to also address if the user had the python file in a directory 
that didn't allow the user to read and write to a file or there isn't enough space on 
the drive to create a file. The program will output "Disk write error". The only thing
that I would like to spend more time on if I wanted to create a full application using 
this program is the appearance of the GUI. Right now there are a few things that look off
on the GUI. Just fine tuning the appearance. Another debugging I had to do was making sure 
the data stayed inside the database after closing the application. In order to make sure
it did I had to use the conn.commit function so that any changes to the database would 
be permanent. 
'''
# Import required Libraries.
from tkinter import *
from tkinter import ttk
import sqlite3
import time


root = Tk()
root.title("Grocery List")

# Initialize database. 
dataCounter = 0
conn = sqlite3.connect('./grocery.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Grocery (item TEXT, qty INTEGER)')
cur.execute('SELECT item, qty FROM Grocery')
itemsInList = StringVar()
for i in cur:
    dataCounter+=1
itemsInList.set("Items In List: " + str(dataCounter))
# Method to add the item into the database
def addItem(*args):
    global dataCounter
    it = itemGrocery.get()
    qt = qtyGrocery.get()
# Split the string
    it = it.lower()
    try:
        it = int(it)
        statusSubmit.set("Error: Invalid Input")
        return
    except:
        pass
    try:
        qt = int(qt)
        add = True
        cur.execute('SELECT item, qty FROM Grocery')
# Check if the item is in the table. If it is update the quantity. 
        for i in cur:
            if it == i[0]:
                cur.execute('UPDATE Grocery SET qty = ? WHERE item = ?', (qt, it))
                dataCounter+=1
                itemsInList.set("Items In List: " + str(dataCounter))
                statusSubmit.set("Completed")
                add = False
        if add == True:
            cur.execute('INSERT INTO Grocery (item, qty) VALUES (?, ?)', (it, qt))
            dataCounter+=1
            itemsInList.set("Items In List: " + str(dataCounter))
            statusSubmit.set("Completed")
    except:
        statusSubmit.set("Error: Invalid Input")
    conn.commit()
    

# Method to export the information into a text file.
def export():
    statusExport.set("")
# Create the output file
    try:
        outputFile = open('GroceryList.txt', 'w')
    except: 
        statusExport.set("Error Writing To Disk")
    cur.execute('SELECT item, qty FROM Grocery')
    outputFile.write("Grocery List")
    outputFile.write("\n")
    outputFile.write("------------")
    outputFile.write("\n")
    for i in cur:
        itemList = i[0]
        quantityList = i[1]
        quantityList = str(quantityList)
        outputString = itemList + ": " + quantityList
        outputFile.write(outputString)
        outputFile.write("\n")
    statusExport.set("Exported")

# Method to delete the items inside the database. 
def deleteItems():
    cur.execute('DROP TABLE IF EXISTS Grocery')
    cur.execute('CREATE TABLE Grocery (item TEXT, qty INTEGER)')
    dataCounter = 0
    itemsInList.set("Items In List: " + str(dataCounter))

def closeProgram():
    exit()

# Initalize the GUI
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

itemGrocery = StringVar()
qtyGrocery = StringVar()
statusExport = StringVar()
statusSubmit = StringVar()

groceryItemEntry = ttk.Entry(mainframe, width=7, textvariable=itemGrocery)
groceryItemEntry.grid(column=1, row=2, sticky=W)
groceryQTYEntry = ttk.Entry(mainframe, width=7, textvariable=qtyGrocery)
groceryQTYEntry.grid(column=3, row=2, sticky=E)


ttk.Label(mainframe, textvariable=statusExport).grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, textvariable=statusSubmit).grid(column=3, row=4, sticky=E)
ttk.Label(mainframe, textvariable=itemsInList).grid(column=2, row=4, sticky=(W, E))
ttk.Label(mainframe, text="Item").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="QTY").grid(column=3, row=1, sticky=E)



ttk.Button(mainframe, text="Submit", command=addItem).grid(column=3, row=3, sticky=E)
ttk.Button(mainframe, text="Export", command=export).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="Clear Database", command=deleteItems).grid(column=3, row=5, sticky=E)
ttk.Button(mainframe, text="Close", command=closeProgram).grid(column=1, row=5, sticky=W)

# Start the main loop of the program. 
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
groceryItemEntry.focus()
root.bind("<Return>", addItem)

root.mainloop()
