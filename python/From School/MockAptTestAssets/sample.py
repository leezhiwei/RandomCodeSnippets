newlist = []
gender = [['M','F'],['Male','Female']]
file = open("DataSet.txt",'r')
str = file.read()
list1 = str.split('\n')
file.close()
header = True
no = 2
count = 0
for sublist in list1:
    if header == True:
        if no == 1:
            header = False
        elif no > 1:
            if count == no - 1:
                header = False
            count += 1
        continue
    newlist.append(sublist.split('-'))
count = 0
totalhr = 0
totalage = 0
mcount = 0
fcount = 0
for sublist in newlist:
    if len(sublist) != 5:
        break
    count += 1
    sublist.append(count)
    totalhr += int(sublist[1])
    totalage += int(sublist[2])
    if gender[0].index(sublist[4]) == 0:
        mcount += 1
    else:
        fcount += 1
avghr = totalhr / count
avgage = totalage / count
x = -1
while x < count:
    if x == -1:
        print('{:<4}{:<12}{:<10}{:<10}{:<15}'.format('No',"Name","Age","Gender","Reason for admission"))
    else:
        print('{:<4}{:<12}{:<10}{:<10}{:<15}'.format(newlist[x][5],newlist[x][0],newlist[x][2],newlist[x][4],newlist[x][3]))
    x += 1
print()
print("The average heart rate is {:.2f}".format(avghr))
print("The average age is {:.2f}".format(avgage))

if mcount > fcount:
    gender = gender[1][0]
else:
    gender = gender[1][1]
print("The most common gender entering the hospital is {}".format(gender))
