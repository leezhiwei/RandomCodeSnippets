'''
Random Number Sum v1.0
Lee Zhi Wei
10/5/2022
'''
import random #Import random module
num1 = random.randint(0,100)#Generate random number between 0 to 100
num2 = random.randint(0,100)#Generate random number between 0 to 100
added = num1 + num2 #Calculate sum of random numbers

useradded = float(input("Enter the sum of {} and {}: ".format(num1, num2))) #Using string formatting, put variables in the input prompt
if useradded == added: #If condition to see if user input is correct or wrong
    print("Correct!")#Print correct statement
else:
    print("Wrong!") #Print wrong statement with answer
    print("The answer is: ", added)
