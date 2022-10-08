'''
CountPush v 1.1
24/5/22
Lee Zhi Wei
'''
pushup = int(input("How many push up is your target? ")) #Prompt for target
totalpush = 0 #Init totalpushups var
days = 0 #Init the days var
dailypush = 0 #Inits dailypush var
while totalpush <= pushup: #While loop
    days += 1 #Increment day
    dailypush = int(input("Day {} : How many pushups did you do today?".format(days))) #Prompts and puts user input in var
    totalpush += dailypush #Adds dailypush var to totalpush var
print("You did a total of {} pushups.".format(totalpush)) #Prints total pushup var
print("You hit your target in {} days!".format(days)) #Prints days used to hit target
