'''
Extremeist v1
5/7/22
Lee Zhi Wei
'''
num_list = [ 10, -13, 50, 5, 7, 65, -40, 44, 30 ] #Number list
def get_extremes(list): #def get extreme
    list.sort() #Sort list
    print(list[0])#Print first val
    print(list[-1]) #Print last val
#def get_extremes(list):
     '''
     smallest = math.inf
     largest = -math.inf
     '''
#    smallest = list[0]
#    largest = list[0]
#    for item in list:
#        if item < smallest:
#            smallest = item
#        if item > largest:
#            largest = item
#    return smallest, largest
get_extremes(num_list) #run def
