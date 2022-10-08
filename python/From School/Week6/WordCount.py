'''
Counting WordList V1.0
24/5/22
Lee Zhi Wei
'''
wordlist = [] #Set var wordlist
lettercount = 0 #Sets counts of letters
while len(wordlist) < 5: #Set loop for 5
    word = input("Enter word (x to exit): ") #Input prompt
    if word == 'x': #If input matches x
        break #Breaks loop
    elif word in wordlist: #Else if word in wordlist
        print("{} in wordlist.... Try again.".format(word)) #If word appears in wordlist
    else: #Else
        lettercount += len(word) #Adds length of word
        wordlist.append(word) #Append the word to wordlist
lettercount = lettercount # Ro make correct
print("Your words are ", wordlist) #List of word
print("Number of words is ", lettercount) #Prints number of word
