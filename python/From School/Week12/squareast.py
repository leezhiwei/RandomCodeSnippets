'''
Square of * v4.4
Lee Zhi Wei
5/7/22
'''
def print_square(side): # print sq def
    for x in range(side): #  for x in range of side
        print('*' * side) # Prints star for amount of side
side = int(input("Input side number: ")) # input side number
print_square(side) # prints the side square
