import pyodbc
import flask
import gen
import urllib
import fakeitem
import random
connection = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};"
                      "Server=localhost\SQLServer2022;"
                      "TrustServerCertificate=Yes;"
                            "Trusted_Connection=Yes", autocommit=True)
cursor = connection.cursor()
try:
    cursor.execute("CREATE DATABASE UserTest")
except:
    print("Database exists, using existing database.")
cursor.execute("USE UserTest")
listoftables = cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'").fetchall()
if len(listoftables) == 0:
    cursor.execute("CREATE TABLE logindetails (UserID VARCHAR(1000) PRIMARY KEY, password VARCHAR(MAX) NOT NULL, UserDesc VARCHAR(MAX), Email VARCHAR(1000) NOT NULL UNIQUE);")
    cursor.execute("CREATE TABLE Transactions (TID INT PRIMARY KEY IDENTITY(1,1), Item1 VARCHAR(MAX) NOT NULL, Item2 VARCHAR(MAX), Item3 VARCHAR(MAX), Item4 VARCHAR(MAX), UserID VARCHAR(1000) FOREIGN KEY REFERENCES logindetails(UserID));")
    profilelist = gen.generator()
    for p in profilelist:
        cursor.execute(f"INSERT INTO logindetails VALUES ('{p[0]}', '{gen.passgen()}', 'Name: {p[1]}, Gender: {p[2]}, Address: {p[3]}, Birthday: {p[5]}','{p[4]}')")
        transnum = random.randint(25000,50000) - 1
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
        if not(transnum % 1000 == 0):
            try:
                cursor.execute(SQLInsert)
            except:
                continue
connection.commit()
sqlinj = flask.Flask(__name__)
@sqlinj.route('/') 
def SQLPage():
    html5="<!DOCTYPE html>"
    htmlstart="<html>"
    head='<head><title>Test your SQL Injection here</title><meta charset="UTF-8"><meta name="description" content="Here is an input prompt."></head>'
    content = '<h1>SQL Test Page</h1> \
    <p>This is a test page with a login prompt</p> \
    <form action="/input">\
    <label for="username">Email:</label> \
    <input type="text" name="username" placeholder="john-doe@gmail.com/johndoe86" required><br><br> \
    <label for="passwd">Password:</label> \
    <input type="password" name="passwd" placeholder="Enter password" required><br>\
    <button type="submit">Logon</button> \
    </form>'
    htmlend = "</html>"
    fullpage = html5 + htmlstart + head + content + htmlend
    return fullpage
@sqlinj.route('/input')
def input():
    username = flask.request.args['username']
    password = flask.request.args['passwd']
    username = urllib.parse.unquote(username)
    password = urllib.parse.unquote(password)
    if '@' in username:
        print(username, password)
        query = f"SELECT UserDesc FROM logindetails WHERE Email = '{username}' AND password = '{password}'"
    else:
        query = f"SELECT UserDesc FROM logindetails WHERE UserID = '{username}' AND password = '{password}'"
    row = connection.execute(query).fetchall()
    if len(row) == 0:
        return "<html><h1>Invalid Login</h1><html>"
    return f"<html><h1>Details of {username}</h1><p>Description:<br>{str(row[0][0])}</h1></html>"
@sqlinj.route('/transhist')
def transac():
    return "<html><h1>Hello</h1></html>"
sqlinj.run()
connection.close()
