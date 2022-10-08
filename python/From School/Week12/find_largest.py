'''
LargestInt v0.5
5/7/22
Lee Zhi Wei
'''
order = ['first','second','third','forth'] # List for order
def find_larger(n1,n2): # Find larger def
    if n1 > n2: # if n1 is more than n2
        return n1 # Return n1
    else: #Else
        return n2 #Return n2
for x in range(4): # for loop
    num = int(input(f"Enter the {order[x]} integer numbr: ")) #Input number
    exec('n' + str(x) + '= num') # assign n(x) value
    if x == 2: # uses def function to find largest
        larger1 = find_larger(n0,n1)
    if x == 3: # uses def function to find largest
        larger2 = find_larger(n2,n3)
largestinteger = find_larger(larger1,larger2) # uses def library to find largest
print(f"The largest integer is {largestinteger}") # Print largest
'''
input1 = int(input("Enter first no. "))
input2 = int(input("Enter second no. "))
input3 = int(input("Enter third no. "))
input4 = int(input("Enter fourth no. "))

larger1 = find_larger(input1,input2)
larger2 = find_larger(input3,input4)
finallarger = find_larger(larger1,larger2)

print('Largest integer is', finallarger)
'''
