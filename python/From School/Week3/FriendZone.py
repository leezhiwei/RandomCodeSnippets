friends = ["Izzat", "Bryan", "Dalton", "Ethan", "Isaac"] # Set list as var
new_friend = str(input("New Friend Name: ")) # Prompt for new friend name
friends.append(new_friend)#Append new friend name to friends list
print(friends)#Print list after append
current_friend = str(input("Current Friend Name to be removed: ")) # Prompt current friend name
index_current = friends.index(current_friend) # puts current friend index as var
print(current_friend, "will be removed. The person's index is ", index_current) #Print current friend index
friends.pop(index_current)#Pops out current friends from list
print(friends)#Print modified list
'''
FZ v1.00
Lee Zhi Wei
5/5/2022
'''
