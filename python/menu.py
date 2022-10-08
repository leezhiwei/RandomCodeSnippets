'''
menu 1.0
Lee Zhi Wei
'''
#Dynamically importing components as I need them cause why not
while True: # while loop
    exitflag = False # exitflag bool
    if exitflag == True: # if its true
        break # break out of outer loop
    print("1. Print Menu\n2. Print Submenu\n3. Do something\n4. Do something else") # print menu selection
    sel = input("What is your selection ") # input ptompt
    try: # exception catching
        selval = int(sel) # try to make it int
    except: # if error
        print("Please input a number") # print error
        continue # restart loop
    if selval == 1: # if 1 
        continue # restart loop
    elif selval == 2: # else if 2
        selval = 1 # make it 1 again
        while True: # start inner loop
            print("Submenu Options\n1. Ascii number generator\n2. Prints web request\n3. Exit") # submenu option
            sel1 = input("Input your selection ") # input prompt
            try: # exception catching
                selval1 = int(sel1) # try and make it int
            except: # if not
                print("Please input a number") # print error
                continue # continue inner loop
            if selval1 == 1: # if 1
                import random # random module
                randval = random.randint(0,256) # from 0 to 256 cause max chars??
                char = chr(randval) # get char from the random value
                print(f'Your random char is {char}') # print char
                exitflag = True # set exitflag
                break # break this loop
            elif selval1 == 2: # if its 2
                import requests # import requests module
                url = input("Input the page you want to get the HTML of ") # get the url input
                if 'http://' or 'https://' in url: # requests don't like if it gets without http or https
                    try: # exception catching
                        r = requests.get(url) # use requests to try and request url
                    except requests.exceptions.SSLError: # if sslerror
                        #import warnings
                        #warnings.filterwarnings('ignore')
                        r = requests.get(url, verify = False) # try again with ssl verification disabled
                    except Exception as e: # if exception occurs
                        print(f"An error occured, error code is {e}") # print error
                        exitflag = True # set flag
                        break # break
                    print(f"The content of the HTML is {r.text}") # print html text
                    exitflag = True # set flag
                    break # break loop
                else: # else if url has no http or https
                    print("Please put http:// or https:// in front of the URL") # tell user
                    continue # continue loop
            elif selval1 == 3: # if option3 
                break # break loop
    elif selval == 3: # option3
        print("Doing something, putting you back in the loop") # do something
        continue # continue loop
    elif selval == 4: # option 4
        print("Doing something else, breaking the loop") # tell use
        break # break loop
    else: # else invalid option
        print("Invalid Option") # prompt user
        continue # continue loop

