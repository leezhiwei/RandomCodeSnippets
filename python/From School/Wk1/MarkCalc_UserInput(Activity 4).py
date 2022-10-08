'''
MarkCalc V1.0(User Input)
21/4/2022
Lee Zhi Wei
'''
CTPer = 30/100 #Setting Common Test Percentage
CAPer = 40/100 #Setting Common Assesment percentage
APer = 30/100 # Setting Assignment Percentage
#User Input
CTMark = float(input("Enter your Common Test Mark here:")) #User input for Common Test Marks
if CTMark > 100: #Sets an if condition to make sure mark is not above 100
    print("The score cannot be more than 100 marks.")
    quit()
AMark = float(input("Enter your Assignment Mark here:"))#User input for Common Test Marks
if AMark > 100:#Sets an if condition to make sure mark is not above 100
    print("The score cannot be more than 100 marks.")
    quit()
CAMark= float(input("Enter your Common Assesment Mark here:"))
if CAMark > 100:#Sets an if condition to make sure mark is not above 100
    print("The score cannot be more than 100 marks.")
    quit()
#Total calculation of all marks
TotalMark= (CTPer*CTMark)+(CAPer*CAMark)+(APer*AMark)
#Printing of the mark out to user
print("Your total mark is :", end=' ')
print(TotalMark, end='')
print("/100")
