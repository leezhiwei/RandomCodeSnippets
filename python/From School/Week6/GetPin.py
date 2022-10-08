'''
GetPin v1.2
24/5/22
Lee Zhi Wei
'''
pin = 23456 #Init var pin
tries = 0 #Init var tries 
correct = False #Init bool
while tries < 3: #While loop
    userinput = int(input("Enter Pin: ")) #Input
    if userinput == pin: #If condition for correct
        print("Correct!") #Print correct
        correct = True #Sets bool to true
        break #breaks out of loop
    else: #Else 
        print("Incorrect") #Prints incorrect
        tries += 1 #Add one to tries
        print("You have {} tries left".format(3 - tries)) #Print amount of tries left
if correct == False: #If incorrect out of loop
    print(pin)
    print("You have no more tries, account locked.")#Print locked account message
    
