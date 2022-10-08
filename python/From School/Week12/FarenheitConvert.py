'''
TempConvert v1.1.1
5/7/22
Lee Zhi Wei
'''
c = int(input("Enter temperature in celsius: ")) # Celcius Input
def convert_temperature(c): #Def for convert temp
    f = (c * 9/5) + 32 #Farenheit convert
    print(f"The temperature in equivalent to {f:.1f} farenheit.") #Print
convert_temperature(c) #Run def
