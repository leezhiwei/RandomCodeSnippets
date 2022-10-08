# Sample GUI Application

# 1. Import tkinter 
from tkinter import *

'''------------------------ Functions --------------------------''' 
# function to compute and display Multiplcation Table
def display_table():
    n = int(entNumber.get())
    txtTable.delete("1.0", END)         # clear the content
    for i in range(1,13):               # i : 1, 2, . . ., 12
        row = "{:3} x {:2} = {:3}\n".format(i, n, i * n)
        txtTable.insert(END, row)       # insert new content

# function to calculate and display BMI
def calc_bmi():
    txtBMI.delete("1.0", END)           # clear the content
    weight = float(entWeight.get())
    height = float(entHeight.get())
    bmi = weight / (height * height)
    txtBMI.insert(END, round(bmi,2))    # insert new content

# function to show a frame
def raise_frame(frame):
    frame.tkraise()
''' ------------------------------------------------------------ '''

# 2. Create main window 
window = Tk()
window.title('Sample GUI Application')
window.geometry('600x400')

''' Frame 1 : Multiplcation Table  '''
f1 = Frame(window, bg='light yellow', width=400, height=300)

# Add widgets
lblTitle1 = Label(f1, text="Multiplcation Table", bg="light yellow", font=('Lucida Calligraphy', 12))
lblNumber = Label(f1, text="Enter number", width=10)
entNumber = Entry(f1, fg='red', width=29)
btnDisplay = Button(f1, text="Display table", width=10, command=display_table)
txtTable = Text(f1, fg='blue', width=22, height=12)

# Organize (lay out) the widgets using place() manager
lblTitle1.place(x=20, y=10)     # column 1, row 1
lblNumber.place(x=20, y=50)     # column 1, row 1
btnDisplay.place(x=20, y=90)    # column 1, row 2
entNumber.place(x=120, y=50)    # column 2, row 1
txtTable.place(x=120, y=90)     # column 2, row 2

''' Frame 2 : BMI Calculator  '''
f2 = Frame(window, bg='light blue', width=400, height=300)

# 3. Add widgets
lblTitle2 = Label(f2, text="BMI Calculator", bg="light blue", font=('Lucida Calligraphy', 12))
lblWeight = Label(f2, text="Weight (kg)", width=12)
lblHeight = Label(f2, text="Height (m)", width=12)
entWeight = Entry(f2, width=20)
entHeight = Entry(f2, width=20)
lblBMI = Label(f2, text="BMI", bg="light yellow", width=12)
txtBMI = Text(f2, width=15, height=1, bg="light yellow", fg="blue")
btnCalculate = Button(f2, text="Calculate", width=10, command=calc_bmi)

# Organize (lay out) the widgets using place() manager
lblTitle2.place(x=20, y=10)     
lblWeight.place(x=20, y=50)
lblHeight.place(x=20, y=90)
lblBMI.place(x=20, y=130)
entWeight.place(x=120, y=50)
entHeight.place(x=120, y=90)
txtBMI.place(x=120, y=130)
btnCalculate.place(x=260, y=130)

''' Main window '''
frmMenu = Frame(window, bg='light grey', width=150, height=300)
lblMenu = Label(frmMenu, text='Main Menu', width=9, fg='blue', bg='light grey', font=('Lucida Calligraphy', 12))
lblMenu.place(x=20, y=10)
btn1 = Button(frmMenu, text='Multiplcation Table', width=15, fg='blue', command=lambda:raise_frame(f1))
btn1.place(x=20, y=50)
btn2 = Button(frmMenu, text='BMI Calculator', width=15, fg='blue', command=lambda:raise_frame(f2))
btn2.place(x=20, y=90)

''' lay out the frames '''
frmMenu.place(x=20, y=20)
f1.place(x=170, y=20)
f2.place(x=170, y=20)

raise_frame(f1)

# 4. Add main event loop (to handle user events)
window.mainloop()
