# Lee Zhi Wei - IT01
newlist = [] # init new list
file = open("DataSet.txt",'r')# open file as read
data = file.read() # read file into data
no = 2 # how many header
header = True # if header present
data_list1 = data.split('\n') # split by newline
count = 0 # init count var
file.close() # close the file
for n in data_list1: # processing
    if header == True: # if header true
        if no == 1: # if no is 1
            header = False # sets header to false
            continue # continues
        elif no > 1: # else if more than 1
            if count != no - 1: # if count is not equal to header number deduct 1
                count += 1 # add one to count
                continue # continue
            else: # else count is more than zero
                header = False # set header to false 
                continue # continue
    newlist.append(n.split('-')) # split by dash
#Part A
#print(newlist)
#Data Manipulation
gender = [['M','F'],['Male','Female']] # gender list by qn
count = 0
totalhr = 0
totalage = 0   # init vars
mcount = 0
fcount = 0
for n in newlist: # for n in newlist
    if len(n) != 5: # when encounter empty list, break
        break
    count += 1 # count for patienr
    n.append(count) # append count
    totalhr += int(n[1]) # add total hr
    totalage += int(n[2]) # add total age
    if gender[0].index(n[4]) == 0: # gender
        mcount += 1 # malecount
    elif gender[0].index(n[4]) == 1:
        fcount += 1 # femalecount
#Averages
avgage = totalage / count # avg age
avghr = totalhr / count # avg hr
#Printing
print("{:<4}{:<15}{:<10}{:<10}{:<15}".format("No","Name","Age","Gender","Reason for admission")) # print header
for n in newlist: # for n in newlist
    if len(n) != 6: # encounter empty list, break
        break
    print("{:<4}{:<15}{:<10}{:<10}{:<15}".format(n[5],n[0],n[2],n[4],n[3])) # print values
print("The average heart rate is {:.2f}".format(avghr)) # avg hr in 2dp
print("The average age is {:.2f}".format(avgage)) #avg age in 2dp
#Common gender
if mcount > fcount: # if m bigger no then f
    cgender = gender[1][0] # common gender is Male
else:
    cgender = gender[1][1] # Else female
print("The most common gender is {}".format(cgender)) # Print commongender
