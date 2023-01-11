import pyodbc
import gen
import urllib
import fakeitem
import random
connection = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};"
                      "Server=localhost\SQLServer2022;"
                      "TrustServerCertificate=Yes;"
                            "Trusted_Connection=Yes", autocommit=True)
cursor = connection.cursor()
cursor.execute("USE UserTest;")
listoftables = cursor.execute("SELECT UserID FROM logindetails;").fetchall()
if True:
    for p in listoftables:
        transnum = random.randint(1000,50000)
        print(f'No of Trans {transnum}')
        SQLInsert = 'INSERT INTO Transactions (Item1, Item2, Item3, Item4, UserID) VALUES '
        for _ in range(transnum):
            valname = ''
            itemno = random.randint(1,5)
            if itemno == 1:
                item = fakeitem.fakeitemname()
                valname += f"('{item}', NULL, NULL, NULL, '{p[0]}')"
            elif itemno > 1:
                iteminfo = []
                for i in range(1,itemno):
                    item = fakeitem.fakeitemname()
                    iteminfo.append(item)
                if len(iteminfo) < 4:
                    nullcount = 4 - len(iteminfo)
                    valname += '('
                    for i in iteminfo:
                        valname += str("'" + i + "'" + ', ')
                    for n in range(nullcount):
                        valname += "NULL, "
                else:
                    valname += '('
                    for i in iteminfo:
                        valname += str("'" + i + "'" + ', ')
                valname += "'" + p[0] + "')"
            if _ % 1000 == 0:
                SQLInsert += valname + ';'
                cursor.execute(SQLInsert)
                SQLInsert = 'INSERT INTO Transactions (Item1, Item2, Item3, Item4, UserID) VALUES '
                continue
            if list(range(transnum))[-1] == _:
                SQLInsert += valname + ';'
            else:
                SQLInsert += valname + ', '
        if not(_%1000==0):
            cursor.execute(SQLInsert)
connection.commit()
connection.close()
