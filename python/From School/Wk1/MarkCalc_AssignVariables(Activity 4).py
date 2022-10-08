'''
MarkCalc V1.2 (Assign Variable)
21/4/2022
Lee Zhi Wei
'''
CTPer = 30/100 #Setting Common Test Percentage
CAPer = 40/100 #Setting Common Assesment percentage
APer = 30/100 # Setting Assesment Percentage
#Assign mark variables
CTMark=60
AMark=80
CAMark=75
#Total calculation of all marks
TotalMark= (CTPer*CTMark)+(CAPer*CAMark)+(APer*AMark)
#Printing of the mark out to user
print("Your total mark is :", end=' ')
print(TotalMark, end='')
print("/100")
