# BMI Calculator

'''----------------------- Function(s) ------------------------'''
def calculate_bmi():
    txtBMI.delete("1.0", END)
    weight = float(entWeight.get())
    height = float(entHeight.get())
    bmi = weight / (height * height)
    txtBMI.insert(END, round(bmi,2))
'''------------------------------------------------------------'''

# 1. Import tkinter 
from tkinter import *        		

# 2. Create main window 
window = Tk()
window.title('BMI Calculator')
window.geometry('400x320')

# 3. Add widgets e.g. Label, Entry, Button, Text
lblWeight = Label(window, text="Weight (kg)", width=20)
entWeight = Entry(window, width=20)
lblHeight = Label(window, text="Height (m) ", width=20)
entHeight = Entry(window, width=20)
lblBMI = Label(window, text="BMI", fg='blue', width=20)
txtBMI = Text(window, fg='blue', bg='yellow', width=15, height=1)
btnCalculate = Button(window, text="Calculate", width=12, command=calculate_bmi)

# organize (lay out) the widgets using place() manager
# Organize (lay out) the widgets using place() manager
lblWeight.place(x=20, y=20)             # row 1, column 1
entWeight.place(x=140, y=20)            # row 1, column 2
lblHeight.place(x=20, y=60)             # row 2, column 1
entHeight.place(x=140, y=60)            # row 2, column 2
lblBMI.place(x=20, y=100)               # row 3, column 1
txtBMI.place(x=140, y=100)              # row 3, column 2
btnCalculate.place(x=280, y=100)        # row 3, column 3

'''
# Organize (lay out) the widgets using grid() manager
lblWeight.grid(row=0, column=0)         # row 1, column 1
entWeight.grid(row=0, column=1)         # row 2, column 2
lblHeight.grid(row=1, column=0)         # row 2, column 2
entHeight.grid(row=1, column=1)         # row 2, column 2
lblBMI.grid(row=2, column=0)            # row 3, column 1
txtBMI.grid(row=2, column=1)            # row 3, column 2
btnCalculate.grid(row=2, column=2)      # row 3, column 3

'''

# 4. Add the main event loop (to handle user events)
window.mainloop()
