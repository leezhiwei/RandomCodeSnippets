'''
Birth Paradox v0.1
7/7/22
Lee Zhi Wei
'''
import random #Random module
print("This program demonstrates the birthday paradox") # Print header
list = [] # init list
attempts = 0 # init attempts
while True: # loop
    attempts +=1 # add one attempt
    day = random.randint(1,365) # random day
    print("{} was randomly generated.".format(day)) #print day generated
    if day in list: #if day in list
            break #break
    list.append(day) # append to list
print("This took {} attempts.".format(attempts)) #print attempts

