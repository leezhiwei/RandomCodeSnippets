# XLSX input description from sql, for use with exact globe
import pyodbc
import openpyxl
filename = 'testwb.xlsx'
server = 'tcp:192.168.1.111' # init variables
database = 'Database1'
cnxn = pyodbc.connect(f'Driver=SQL Server;Server={server};Database={database};Trusted_Connection=yes;') # create connection, can use SQL username or password, currently using Windows Authentication
cursor = cnxn.cursor() # set cursor
workbook = openpyxl.load_workbook(filename) # open workbook
sheet = workbook.worksheets[0] # use first sheet
rowamt = len(sheet['A']) # get how many item codes in a row
for rownum in range(1,rowamt): # for loop between A1 and A{rowamt}
    itemcode = str(sheet[f'A{rownum}'].value) # get the itemcode
    print(f'Item code is {itemcode}') # prints it out
    cursor.execute("SELECT Description FROM dbo.Items WHERE ItemCode = " + "'" + itemcode + "'") # do a select statement where itemcode = {itemcode}
    row = cursor.fetchone() # Fetch the only row, Description
    if not row: # if nonetype, eg itemcode dont exist
        output = '' # output is blank
    else: #Else if its a value
        output = row.Description # get the output
    output = str(output) # put it in a variable and string it, in case it is a number
    print(f"Item Description is {output}") # print item description out
    sheet[f'B{rownum}'].value = output # set the next column as the Description
sel = input("Do you want to save? ") # ask if want to save
sel = sel.capitalize() # makes it 'Yes'
if sel[0] == 'Y': # if first letter is 'Y'
    workbook.save(f'Modified_{filename}') # save the file under a different name
else: # else other value
    print("Not saved") # dont save
    exit() # exit script
