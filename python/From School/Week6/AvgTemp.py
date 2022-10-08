'''
AvgTemp v1.2
24/5/22
Lee Zhi Wei
'''
temp_list = [ 20.5, 22, 21, 29.3, 28.2, 25, 26, 28, 26.3, 25.6, 29.3, 28.4, 24.5, 26.3, 25.5, 26.5, 23.3, 24.3, 25.4, 26.5, 23,3, 25.4, 26.3, 25.5 ]
#List of temps
numoftemps = len(temp_list) #Get number of elements in list
loopval = 0 # Loopvalue var
totaltemp = 0 # Totaltemp var
print("Number of readings : ", numoftemps) # Prints number of readings
while loopval < numoftemps: #While loop when loopval lesser than number of temps
    totaltemp += temp_list[loopval] # Adds value to Totaltemp var
    loopval += 1 # Adds one to loopvalue
avgreading = totaltemp / numoftemps #Calcs avg reading
rounded = round(avgreading, 2) #Round it to 2dp
print("The average temperature is ", rounded) #Prints rounded value
