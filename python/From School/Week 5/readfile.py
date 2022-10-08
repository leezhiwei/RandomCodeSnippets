'''
Readfile v1.0
20/5/22
Lee Zhi Wei
'''
datapath = 'D:\\PRG1_data\\' #Sets path to file
file = open(datapath + 'todolist.txt','r') #Sets open as a var
for x in range(3): #For loop
    print(file.readline())#Prints line 
    x += 1 #Increment x
