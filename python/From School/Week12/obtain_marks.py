'''
Obtain_Marks V2
Lee Zhi Wei
14/7/22
'''
mark_list = [['Mary', 90.5], ['Charles', 60.4], ['John', 70.5], ['Javier', 32.0], ['Luke', 46.7]]
def obtain_grade(marks):
    if marks >= 84.5:
        return 'A+'
    elif 79.5 <= marks < 84.5:
        return 'A'
    elif 74.5 <= marks < 79.5:
        return 'B+'
    elif 69.5 <= marks < 74.5:
        return 'B'
    elif 64.5 <= marks < 69.5:
        return 'C+'
    elif 59.5 <= marks < 64.5:
        return 'C'
    elif 54.5 <= marks < 59.5:
        return 'D+'
    elif 49.5 <= marks < 54.5:
        return 'D'
    else:
        return 'F'
print("{:<15}{:<10}{:<10}".format("Student Name","Marks","Grade"))
for sublist in mark_list:
    print("{:<15}{:<10}{:<10}".format(sublist[0],sublist[1],obtain_grade(sublist[1])))
