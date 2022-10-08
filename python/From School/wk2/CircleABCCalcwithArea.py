import math #Import math module
a = float(input("Enter value of a: "))#User input of a
b = float(input("Enter value of b: "))#User input of b

c = math.sqrt(math.pow(a, 2) + math.pow(b, 2)) #Calculate c using pythagoras' theorem

print("C is: ", c) #Print out c

rad = c/2 #Radius from c
radsq = math.pow(rad, 2) #Radius squared variable


area = (math.pi * radsq) #Area of circle by pi*(r^2)
print("Area is: ", area)#Print area of circle

'''
Right angled ABC with circle area v1.0.5
Zhi Wei
'''
