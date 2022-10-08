# Multiplication Table

''' ------------------------ Function -------------------------- '''
def display_table():
    n = int(entNumber.get())
    txtTable.delete("1.0", END)
    for i in range(1,13):         # i : 1, 2, . . ., 12
        row = "{:3} x {:2} = {:3}\n".format(i, n, i * n)
        txtTable.insert(END, row)
''' ------------------------------------------------------------ '''

# 1. Import tkinter 
from tkinter import *        		

# 2. Create main window 
window = Tk()			 		
window.title("Multiplication Table")
window.geometry('400x320')

# 3. Add widgets e.g. Label, Entry, Button, Text
lblNumber = Label(window, text="Enter number", width=10)
entNumber = Entry(window, fg='red', width=29)
btnDisplay = Button(window, text="Display table", width=10, command=display_table)
txtTable = Text(window, fg='blue', width=22, height=12)

# Organize (lay out) the widgets using place() manager
lblNumber.place(x=20, y=20)     # row 1, column 1
entNumber.place(x=120, y=20)    # row 1, column 2
btnDisplay.place(x=20, y=60)    # row 2, column 1
txtTable.place(x=120, y=60)     # row 2, column 2

# 4. Add the main event loop (to handle user events)
window.mainloop()
