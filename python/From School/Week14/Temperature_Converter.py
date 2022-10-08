# Temperature Converter

# 1. Import tkinter  
from tkinter import *        		

''' ------------------------ Functions ------------------------- '''
def convert_CtoF():
    c = float(entCelsius.get())
    f = c * 9 / 5 + 32
    entFahrenheit.delete(0, END)
    entFahrenheit.insert(0, "{:.1f}".format(f))  

def convert_FtoC():
    f = float(entFahrenheit.get())
    c = (f - 32) * 5 / 9 
    entCelsius.delete(0, END)
    entCelsius.insert(0, "{:.1f}".format(c))
''' ------------------------------------------------------------ '''

# 2. Create main window 
window = Tk()			 		
window.title("Temperature Converter")
window.geometry('360x240')

# 3. Add widgets e.g. Label, Button, Entry
lblCelsius = Label(window, text="Temperature (Celsius)", width=20)
lblFahrenheit = Label(window, text="Temperature (Fahrenheit)", width=20)

entCelsius = Entry(window, width=24, justify='center')
entFahrenheit = Entry(window, width=24, justify='center')

btnConvert_CtoF = Button(window, text="Convert C to F", width=20, command=convert_CtoF)
btnConvert_FtoC = Button(window, text="Convert F to C", width=20, command=convert_FtoC)

# lay out the widgets using place() manager
lblCelsius.place(x=20, y=20)
lblFahrenheit.place(x=160, y=20)
entCelsius.place(x=20, y=50)
entFahrenheit.place(x=160, y=50)
btnConvert_CtoF.place(x=20, y=80)
btnConvert_FtoC.place(x=160, y=80)
'''
# lay out the widgets using grid() manager
lblCelsius.grid(row=0, column=0)
lblFahrenheit.grid(row=0, column=1)
entCelsius.grid(row=1, column=0)
entFahrenheit.grid(row=1, column=1)
btnConvert_CtoF.grid(row=2, column=0)
btnConvert_FtoC.grid(row=2, column=1)
'''

# 4. Add window.mainloop()
window.mainloop()
