'''
LetterCount V1.2
Lee Zhi Wei
14/7/22
'''
dict = {} # declare dict
sen = input("Input a sentence: ") #Input
senlower = sen.lower() # lower whole sentence
for char in senlower: # for char in senlower
    if char.isalpha(): # is alphabet
        if dict.get(char,None) == None: # if dont exist in dict
            dict[char] = 0 # Assign new var
        dict[char] += 1 # plus 1
for i in dict: # print for i in dict
    print(f"{i} : {dict[i]}") # prints the number 
'''
for char in sen:
    print(char)
    if char.isalpha():
        if char in letters:
        letters[char] += 1
    else:
        letters[char] = 1
print(letters)
for item in letters:
    print("{:s} : {:d}".format(item, letters[item]))
'''
