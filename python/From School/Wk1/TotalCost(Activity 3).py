'''
Item Calc
v1.0 - 21/4/22
Lee Zhi Wei
'''
item = 250 #Setting vars
gst = 7/100 #GST setting in %

itemcosttotal = item * gst + item #Processing the cost
print("The total cost of the item is ", end='$') #Print readable statement
print(itemcosttotal) #Print total amount with GST
