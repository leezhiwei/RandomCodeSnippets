'''
LeapCalc v1.00
Lee Zhi Wei
12/5/2022
'''
year = int(input("Please enter the year: ")) #Prompt user for input

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: #If statement if year is divisible by 4 and not divisible by 100 or divisible by 400
    print(year, "is a leap year.")
else: #Else condition for not leap year
    print(year, "is not a leap year.")
