'''
Hello Christmas V99.9
Lee Zhi Wei
28/6/22
'''
char = input("Enter a character:") #Input char
num = int(input("Enter a number:")) + 1 # Number of rows
for x in range(num): #For loop
    print(' ' * (num-x),end='') #print spaces
    print((char + ' ') *x) #Prints char
print("Merry Christmas") #Print ending message


'''# Nested for
for row in range(num):
    spos = num - row - 1 #leading space
    for i in range(spos):
        print(" ", end='')
    for column in range(row+1):
        print(char, end=' ')
    print()
'''
