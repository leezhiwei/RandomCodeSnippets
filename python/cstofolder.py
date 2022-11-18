import os
import datetime
import shutil
list = []
VSProjFolder = 'D:\School Stuff\VSProjs'
try:
    weekno = int(input("What is the week number:  "))
except:
    print("Please enter a valid week number")
    quit()
OutputFolder = f'D:\School Stuff\PRG2(C#)\Week {weekno}'
dirlist = os.listdir(VSProjFolder)
for directory in dirlist:
    mdate = datetime.date.fromtimestamp(os.path.getmtime(f'{VSProjFolder}\{directory}'))
    dur = datetime.date.today() - mdate
    if dur < datetime.timedelta(days = 5):
        print(f"{directory} is less than 5 days old")
        list.append(directory)
if len(list) == 0:
    print("No directory available")
    exit()
else:
    userinput = input(f"Do you want to copy the CS files of the following directories? {list} ")
    if userinput.upper() == 'Y':
        for dir in list:
            shutil.copyfile(f'{VSProjFolder}\{dir}\{dir}\Program.cs',f'{OutputFolder}\{dir}.cs')
            dirlist = os.listdir(f'{VSProjFolder}\{dir}\{dir}')
            for files in dirlist:
                if '.' in files:
                    splitted = files.split('.')
                    if splitted[1] == 'cs':
                        shutil.copyfile(f'{VSProjFolder}\{dir}\{dir}\{files}',f'{OutputFolder}\{files}')
                    elif splitted[1] == 'csv':
                        shutil.copyfile(f'{VSProjFolder}\{dir}\{dir}\{files}',f'{OutputFolder}\{files}')
        print('Done')
    else:
        print("Goodbye")
        exit()
