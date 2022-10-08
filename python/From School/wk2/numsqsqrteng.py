import math #Import math module
print('{} \t {} \t {} \t {}'.format('Number', 'Square', 'Square root', 'English')) #Print header
num = 0 #Set num's inital value
for num in range(5): #For loop
    num = num + 1#Adds one to num
    sq = int(math.pow(num, 2))#Square's num
    sqrt = math.sqrt(num)#Squareroot num
    if num == 1:#If num is equal to 1, print one
        english = 'One'
    elif num == 2:#If num is equal to 2, print two
        english = 'Two'
    elif num == 3:#If num is equal to 3, print three
        english = 'Three'
    elif num == 4:#If num is equal to 4, print four
        english = 'Four'
    elif num == 5:#If num is equal to 5, print five
        english = 'Five'
    print('{} \t {:>4d} \t\t {:.2f} \t \t {:>7}'.format(num, sq, sqrt, english))
    #Print formatting with tabs 
