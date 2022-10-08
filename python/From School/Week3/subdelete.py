'''
Subremove v1.0.0
29/4/22 Zhi Wei
'''
origstring = input(str("Enter string: ")) #Prompt for Original string
subtodel = input(str("Substring to del: ")) #Prompt for substring to delete

modstring = origstring.replace(subtodel, "") #created var called modstring that will replace subtodel variable with blank space

print("Modified string is : " + modstring) #Printed modified string
