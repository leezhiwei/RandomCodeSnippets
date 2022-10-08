'''
GuardGame V1.0
Lee Zhi Wei
10/5/2022
'''
yesorno = str(input("Does guard see the player?(y/n) ")) #prompt user for input

if yesorno == 'y': #If condition with yes
    guarddist = float(input("How far is the guard away? "))#Prompt user for guard distance
    if guarddist <= 1:
        print("Attacked! Boom.")
    elif 2 <= guarddist <= 4:
        print("Will advance!")
    elif guarddist >= 5:
        print("Will wait!")         #Condition checking
    else:
        print("Invalid input")
elif yesorno == 'n':
    print("Will wait!") # If condition with no
else:
    print("Invalid input!") #Sanity check
