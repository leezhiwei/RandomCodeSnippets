'''
Appendfile v1.0
20/5/22
Lee Zhi Wei
'''
fileloc = 'D:\\prices.txt' #File location
file = open(fileloc,'a') #Set open variable
prices = [["teh peng", 1.2],["milo peng", 1.4]] #Price list

for x in range(2): #For loop
    file.write(prices[x][0]) #Append name
    file.write(": $") #Append colon dollar sign
    file.write(str(prices[x][1])) #Sets price to str
    file.write("\n") #Newline
    x += 1 #Increment x
file.close() #Close file
