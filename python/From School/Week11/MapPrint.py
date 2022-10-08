'''
MapPrint v2.65
Lee Zhi Wei
28/6/22
'''
x = 0
H = True
map =[['T', ' ', ' ', ' ', 'T'],[' ', 'P', ' ', ' ', ' '],[' ', ' ', ' ', 'T', ' '],[' ', 'T', ' ', ' ', ' ']]
header = '+---' * (len(map)+ 1) + '+'

while x < len(map[0]):
    if H == True:
        print(header)
        H = False
        continue
    else:
        if x == len(map):
            break
        y = 0
        while y < len(map[x]):
            print('|{:^3}'.format(map[x][y]), end = '')
            if y == len(map[x]) - 1:
                print('|')
            H = True
            y += 1
    x += 1
'''
num_row = len(map)
num_column = len(map[0])
for column in range(num_column):
    print('+---', end = '')
print('+')
for row in range(num_row):
    for column in map[row]:
        print("| {}".format(column),end = '')
    print('|')
    for column in range(num_column):
        print("+===", end='')
    print('+')
'''
