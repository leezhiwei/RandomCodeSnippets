'''
Square of char v4.4
Lee Zhi Wei
5/7/22
'''
def print_square(side,char): # defin with the 2 var
    for x in range(side): # for x in range of side
        print(char * side) # prints char times the side times
side = int(input("Input side number: ")) # Input side no
char = str(input("Input character: ")) # input character
print_square(side,char) #Call for def
