'''
Timestable v2.0.1
24/5/22
Lee Zhi Wei
'''
numbertotimes = float(input("Please enter a number: ")) #Prompt for the first number
mul = 0 #Inits multiplied by variable
while mul < 10: #While loop
    mul += 1 #Add one to mul var
    end = numbertotimes * mul # Multiplies initial number and multiplied number to form end number
    print("{} x {} = {}".format(numbertotimes, mul, end)) #Prints final values
