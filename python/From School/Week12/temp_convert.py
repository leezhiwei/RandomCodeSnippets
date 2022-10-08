'''
Tempconvert V 2.5
Lee Zhi Wei
14/7/22
'''
def fartocel(f):
    c = 5.0/9.0 * (f - 32)
    return c
def celtofar(c):
    f = 9.0/5.0 * c + 32
    return f
def menu():
    choice = ['','Farenheit to Celsius','Celcius to Farenheit','Exit']
    print("Temperature Conversion")
    for x in range(4):
        if x == 0:
            continue
        print("[{}]{}".format(x,choice[x]))
while True:
    menu()
    choice = int(input("Please enter your option: "))
    if choice == 3:
        break
    elif choice == 1:
        ftemp = float(input("Please enter your temperature in Farenheit: "))
        print("The temperature in celcius is {} degrees".format(round(fartocel(ftemp),1)))
    elif choice == 2:
        ctemp = float(input("Please enter your temperature in Celcius: "))
        print("The temperature in farenheit is {} degrees".format(round(celtofar(ctemp),1)))
    else:
        print("Invalid Choice")
