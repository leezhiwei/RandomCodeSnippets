'''
OrderMenu v0.1
Lee Zhi Wei
14/7/22
'''
#pricelist var
prices = {'chicken': 8.50,\
          'steak': 13.80,\
          'fish': 9.80,\
          'pasta': 9.50,\
          'coffee': 2.50,\
          'tea':1.80,\
          'water':0.50}
dict = {} # Dictionary var
totalcost = 0 # Totalcost var


def menu():
    choice = ['','Add order','Summarize orders','Quit'] # choice list
    x = 0
    while x < 5:
        if x == 0 or x == 4:
            print("{:18}".format("-" * 18))     #Define menu, header
        else:
            print("{}".format(x),end = '')
            print("{:16}".format('. ' + choice[x]))
        x += 1
while True: # infinte loop
    menu()
    choice = int(input("Your Choice? ")) #Choice
    if choice == 1: # order
        for x in range(2):
            if x == 0: # print header
                print("{:<12}{:<12}".format("-" * 4, '-' * 5))
            else:
                print("{:<12}{:<12}".format("Item", "Price"))
        for i in prices: # print the prices and items
            print("{:<12}${:<12.2f}".format(i.capitalize(), prices[i]))
        order = input("Your order? ") # get user input
        if order in prices: # if order in dictionary
            sets = int(input("How many sets? ")) # ask for amt of sets
            if order not in dict: # if order not in order dictionary
                dict[order] = 0 # add key
            dict[order] += sets # add value
        else: # else 
            print("{} not available".format(order)) # choice is not available
            continue
        print("{} sets of {} ordered".format(sets,order)) # says choice and how many sest
    elif choice == 2: # summarise
        if len(dict) == 0: # if length of order is zero
            print("Orders are empty") #print that dictionary is empty
            continue
        print("{:<12}{:<12}".format("Item", "Quantity")) #Else will print header
        print("{:<12}{:<12}".format("-" * 4, '-' * 8))
        for i in dict: # Captialise the orders and show quantity
            print("{:<12}{:<12}".format(i.capitalize(), dict[i]))
        for i in dict: # loop through dict
            totalcost += prices[i] * dict[i] # find price from price list, multiply with sets
        print("Total cost = ${:.2f}".format(totalcost)) # prints total cost
    elif choice == 3: # if quit
        break # break
    else: # else, choice is not 1, 2, 3
        print("{} is not a selectable option".format(choice)) # print that it is not selectable
