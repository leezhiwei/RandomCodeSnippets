'''
wordfile v1.0
31/5/2022
Lee Zhi Wei
'''
filename = input("Enter filename: ")#Input prompt for filename
file = open(filename) #Var for opening file
lines = 0
words = 0 #Variable init
chars = 0
print("---------------------------Content of file--------------------------") #Header
for line in file:# For the amount of lines in file
    wordsplit = line.split() #Split the words into a list
    lines += 1 #Adds one to lines var
    words += len(wordsplit) #Amount of words(length) in wordlist
    chars += len(line) #Length of character in "Line" variable
    print(line, end='') #Print one line and ends with space
file.close()#Close file
print("--------------------------------------------------------------------") #Back of text
print("Total lines: ", lines) #Print amount of lines
print("Total words: ", words) #Prints amount of words
print("Total Characters: ", chars) #Prints amount of char
