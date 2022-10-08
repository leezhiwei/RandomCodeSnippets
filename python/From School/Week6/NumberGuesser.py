'''
NumberGuess v1.2.2
25/5/22
Lee Zhi Wei
'''
import random #import random module
randnum = random.randint(1,100) #Sets random number as variable
guesses = 0 #Initialised amount of guesses variable
won = False #Initialised winning variable
print("Welcome to Random Number Guess") #Prints welcome message
while guesses < 5: #While guess is less than 5
    guesses += 1 #Increment guess number
    if guesses == 1: #If guesses equals to one
        guess = int(input("Try {}: Enter number between 1-100 (or -1 to end): ".format(guesses))) #Prompts user using inital prompt
        if guess > 100:#Sanity check not more than 100
            print("Not more than 100.")#Prints not more than 100
            break#breaks out of loop
    else:#Else for try again statment
        guess = int(input("Try {}: Guess again, enter number between 1-100 (or -1 to end): ".format(guesses)))# Prompt for try again prompt
        if guess > 100:#Sanity check not more than 100
            print("Not more than 100.")#Prints not more than 100
            break#Breaks out of loop
    if guess == -1:#Escape value
        break#Breaks out of loop
    if guess == randnum:#Winning condition
        won = True #Sets boolean true
        break#Breaks out of loop
    else:#Else for wrong value
        if guess > randnum:#Too high condition
            print("{} is too high".format(guess))#Print value is too high
        elif guess < randnum:#Too low condition
            print("{} is too low".format(guess))#Print value is too low
if won == True:#Winning condition
    print("You got it! The value is {}.".format(randnum))#Congratulatory message
elif guesses == 5:#Failed condition
    print("Unfortunately, you did not get the answer. The correct value is {}".format(randnum))#Failed message
print("Bye. Thanks for playing.")#Goodbye message
