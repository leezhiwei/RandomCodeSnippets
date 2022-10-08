'''
Writeprice v1.0
20/5/22
Lee Zhi Wei
'''
file = 'D:\\prices.txt' #File Destination
prices = [ ["kopi", 0.4], 
           ["teh", 0.4],        #Price list
           ["milo", 0.5], 
           ["soft drinks", 1.20] ]
filevar = open(file,'w') #Set open as a var
for x in range(4): #for loop
    filevar.write(prices[x][0]) #Prints x element in list with the first element of the sublist
    filevar.write(": ") #Prints colon
    filevar.write("$") #Prints dollar sign
    filevar.write(str(prices[x][1])) #Convert price to str. If not error
    filevar.write("\n") #Prints new line
    x += 1 #Increment loop
filevar.close() #Closes file

