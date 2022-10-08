'''
UniqueNo v1.0
31/5/22
Lee Zhi Wei
'''
numbers = [2, 7, 11, 6, 7, 3, 17, 7, 12, 41, 8, 11, 13, 10, 15] #Value List
list = [] #Declare List
for n in numbers: #For loop 
    if len(list) == 5:
        break #Breaks out of loop when list is 5.
    if n % 2 != 0: #Odd number
        if list.count(n) == 1: #If present in list will continue
            continue
        list.append(n) #Append new value to list
print(list) #Print list
