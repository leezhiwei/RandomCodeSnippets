'''
Grade v1.0
Lee Zhi Wei
10/5/2022
'''
grademessage = "You have a grade of" #Standard Grade message
marks = float(input("What is your marks: ")) #User input of grade
if marks >= 85:
    print(grademessage,"A+")
    print("Comment: Excellent!")
elif marks >= 80:
    print(grademessage,"A")
    print("Comment: Well done.")
elif marks >= 75 :
    print(grademessage,"B+")
elif marks >= 70:
    print(grademessage,"B")             #If and elif conditions for grade checking
elif marks >= 65:
    print(grademessage,"C+")
elif marks >=60:
    print(grademessage,"C")
elif marks >=55:
    print(grademessage,"D+")
elif marks >=50:
    print(grademessage,"D")
elif marks < 50:
    print(grademessage, "F")
    print("Comment: See Me")
else:  #Sanity check for invalid input
    print("Invalid input")
    
