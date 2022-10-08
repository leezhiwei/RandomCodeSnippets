'''
OddOrEven v1.00
31/5/22
Lee Zhi Wei
'''
numberlist = [] #Initialise number list
total = 0 #Initialise total value
oddno = []#Init oddno list
evenno = []#Init evenno list
while True: #Infinite while loop
    number = int(input("Enter a number (0 to end): "))#Input prompt
    if number == 0:#if number is zero, break out
        break
    else:#Appends number to numberlist
        numberlist.append(number)
for n in numberlist:#for number in numberlist
    if n % 2 == 0:#Even number
        evenno.append(n)#Append to even list
        total += n# adds number to total number
    else:
        oddno.append(n)#Appends to odd list
        total += n #Add to total number
evenno.sort()#Sort number
oddno.sort()#Sort number
print("Odd Numbers: ", oddno) #Print list odd
print("Even Numbers: ", evenno)#Print list even
average = total / len(numberlist)#Calculate average
print("Average is " , average)#Print average
