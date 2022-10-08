'''
Seconds to H, M, S v1.0
Zhi Wei
'''
seconds = float(input('Please enter time in seconds: '))#Input from user
hours = int(seconds // 3600) # Second floor divide by 60*60 to hours
minutes = int((seconds // 60)- hours*60)# Minutes minus the hour already calculated
secdis = int((seconds - hours*3600 - minutes *60))#Second Displayed seconds minus hours multiplied by 3600 minus minutes multiplied by 60

print(hours, " hr", ", ", minutes, "min , ", secdis, "sec") # Print the regular outputs

