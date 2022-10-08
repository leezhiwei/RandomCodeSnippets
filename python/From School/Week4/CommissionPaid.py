'''
Commissioncalc v1.0
Lee Zhi Wei
10/5/22
'''
MSales = float(input("Monthly sales of the agent: ")) #Prompt for Monthly sales, set as var

if MSales >= 10000: #If condition for more than 10000
    CRate = 0.10
else:
    CRate = 0.05
print("Your commission rate is ", CRate * 100, "%") #Print commision rate
CPaid = CRate * MSales #Calculate for commission paid
print("Commission paid is: $", CRate * MSales)#Print commission paid
