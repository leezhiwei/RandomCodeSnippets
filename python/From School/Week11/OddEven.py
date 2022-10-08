'''
OddEven V1.5.2
Lee Zhi Wei
28/6/22
'''
oddnum = []
evennum =[] #Init vars
avgnum = 0
while True:# While loop
    numbercurrent = int(input("Please enter a number (0 to end): ")) #Input prompt
    if numbercurrent == 0:
        break #Break if 0
    else:
        if numbercurrent % 2 == 0: #num mod 2 is even
            evennum.append(numbercurrent)
            avgnum += numbercurrent #Add num to avg
        else: #Else is odd
            oddnum.append(numbercurrent)
            avgnum += numbercurrent #Add num to avg
oddnum.sort()#Sort the list
evennum.sort()#Sort the list
avgnum = avgnum / (len(oddnum) + len(evennum))#Calc avg num
print("Odd Numbers:" , oddnum)#Print odd no
print("Even Numbers:", evennum)#Print even no
print("Average =", avgnum)#Print avg number
