'''
DriveUpload V1.2.2
Lee Zhi Wei
30/8/22
'''
from pydrive.drive import GoogleDrive # import google drive module from pydrive
from pydrive.auth import GoogleAuth # import google authentication from pydrive
gauth = GoogleAuth() # assign GoogleAuth fn to a var
'''
Zip finder
'''
def zipcheck(): # define function
    import os # import os module
    filelist = [] # init variable of a file list
    count = 0 # count of file
    currentdirlist = os.listdir('./') # list the directory
    for items in currentdirlist: #for each item (eg files and folders)
        if '.' in items: # if the name has a dot (its a file)
            filelist.append(items) # append to other list
    for file in filelist: # for each file in filelist
        templist = file.split('.') # split string by the dot
        extension = templist[1].upper() # upper the file extension
        if extension == 'ZIP': # if its a zip file
            foundfile = templist[0] + '.' + templist[1] # append to a foundfile variable
            count += 1 # increment file count by 1
        else: # if its not a zip
            continue # continue loop
    if count > 1: # if more than 1 zips
        print("Multiple zip files found, check current working directory.") # print error
        return False,'' # return tuple with False and blank string
    try: # catch exception if no zip files found
        print(f'Found file {foundfile}') # try to print name of zip found
        return True,foundfile # and return tuple with True and filename
    except NameError: # if variable not found
        print("Zip file not found, please check current working directory.") # print error
        return False,'' # return tuple with False and empty string
def checkcreds(): # check for credentials.txt
    import warnings #import warning module
    warnings.simplefilter("ignore") # silence any upcoming warnings, cause next line will produce a UserWarning if credentials.txt not present
    gauth.LoadCredentialsFile("credentials.txt") # try and load credential file
    if gauth.credentials is None: # if no credentials are loaded
        return False # return False
    else: # if credentials received is not blank
        return True # return True
def savecreds(): # function to save credentials to credentials.txt
    try: # catch exception if no client_secret.json is present
        gauth.CommandLineAuth() # try and do command line auth
    except: # if json not present
        print("Please provide a client_secrets.json file in the current working directory.") # give error
        exit() # exit script
    gauth.SaveCredentialsFile("credentials.txt") # saves creds to txt
def savefile(filename): # savefile function
    uploadfile = drive.CreateFile({'title': f'{filename}'}) # create the file in drive
    uploadfile.SetContentFile(f'./{filename}') # point to content on local drive
    uploadfile.Upload() # upload the file
    return # returns nothing
output = zipcheck() # output the tuple to another var
if output[0]: # if index 0 of output is True
    foundfile = output[1] # will take filename as index 1
    # pydrive auth
    if checkcreds() == False: # if checkcred function returns False
        savecreds() # Will use savecreds function to save credentials to current dir credentials.txt
    else: # if checkcred function returns True
        gauth.LoadCredentialsFile("credentials.txt") # load credentials file
    drive = GoogleDrive(gauth) # set drive var with the google authentication
    # try to upload
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList() # get list of files in root directory
    for file in file_list: # for fileinfo in the list
        filetitle = file['title'] # get each file name in drive from the "file" dictionary
        if filetitle == foundfile: # if file name matches the zip
            choice = input("Do you want to upload additional copies? (Y/N)") # prompt if want to make additional copies in drive
            choice = choice.upper() # if user enter selection, upper case it
            if choice == 'Y': # if yes 
                savefile(foundfile)# continue upload
                exit() # exit
            elif choice == 'N': # if no
                exit() # exit
            else: # if not choice above
                print("Invalid choice.") # say invalid choice
                exit() # exit
    savefile(foundfile) # if no matching file in drive, just save
    exit() # and exit
                
    


