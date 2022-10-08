'''
Even v1.5
5/7/22
Lee Zhi Wei
'''
num_list = [ 10, -13, 50, 5, 7, 24, 65, -40, 44, 30 ] # Number list
def is_even(n): # define
    if n % 2 == 0: #if even
        return(True) # Return true
    else:
        return(False) #Else return false
for num in num_list: # number in list
    print(is_even(num)) # print true or false
'''
for num in num_list:
    if is_even(num) == True:
        print(num)
'''
