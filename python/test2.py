while True:
    exitflag = False
    if exitflag == True:
        break
    print("1. Print Menu\n2. Print Submenu\n3. Do something\n4. Do something else")
    sel = input("What is your selection ")
    try:
        selval = int(sel)
    except:
        print("Please input a number")
        continue
    if selval == 1:
        continue
    elif selval == 2:
        selval = 1
        while True:
            print("Submenu Options\n1. Ascii number generator\n2. Prints web request\n3. Exit")
            sel1 = input("Input your selection ")
            try:
                selval1 = int(sel1)
            except:
                print("Please input a number")
                continue
            if selval1 == 1:
                import random
                randval = random.randint(0,256)
                char = chr(randval)
                print(f'Your random char is {char}')
                exitflag = True
                break
            elif selval1 == 2:
                import requests
                url = input("Input the page you want to get the HTML of ")
                if 'http://' or 'https://' in url:
                    try:
                        r = requests.get(url)
                    except requests.exceptions.SSLError:
                        #import warnings
                        #warnings.filterwarnings('ignore')
                        r = requests.get(url, verify = False)
                    except Exception as e:
                        print(f"An error occured, error code is {e}")
                        exitflag = True
                        break
                    print(f"The content of the HTML is {r.text}")
                    exitflag = True
                    break
                else:
                    print("Please put http:// or https:// in front of the URL")
                    continue
            elif selval1 == 3:
                break
    elif selval == 3:
        print("Doing something, putting you back in the loop")
        continue
    elif selval == 4:
        print("Doing something else, breaking the loop")
        break
    else:
        print("Invalid Option")
        continue

