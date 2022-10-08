'''
Invert v1.2.5
Lee Zhi Wei
14/7/22
'''
file = open('colours.csv','r')
var = file.read()
firstsplit = var.split('\n')
secondsplit = []
colors_dict = {}        #Variables
new_colors = {}
file.close()
for i in firstsplit:
    secondsplit.append(i.split(',')) # CSV to list
for i in range(len(secondsplit)):
    colors_dict[secondsplit[i][0]] = secondsplit[i][1] # assign new variable in color_dict, Tom as Key, Red as Value
for i in colors_dict:
    if new_colors.get(colors_dict[i],None) == None: # if Red key does not exist in dictionary
        new_colors[colors_dict[i]] = [i] # Makes new key
    else:
        new_colors[colors_dict[i]].append(i) #Else appends
print(new_colors)
'''
is_header = False
for line in data_file:
    if is_header:
        is_header = False
        continue
    line = line.strip('\n')
    line_data = line.split(',')

    colors_dict [line_data[0]] = line_data[1]
data_file.close()

print(colors_dict)
for name in colors_dict:
    colour = colours_dict[name]

    if color in new_colours:
        name_list = new_colors[color]
    else:
        name_list = []

    name_list.append(name)
    new_colors[color] = name_list
        
'''
