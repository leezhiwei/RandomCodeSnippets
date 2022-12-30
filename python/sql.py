import sqlite3
import flask
sqlinj = flask.Flask(__name__)
@sqlinj.route('/') 
def SQLPage():
    html5="<!DOCTYPE html>"
    htmlstart="<html>"
    head='<head><title>Test your SQL Injection here</title><meta charset="UTF-8"><meta name="description" content="Here is an input prompt."></head>'
    content = "<h1>SQL Test Page</h1>"
    htmlend = "</html>"
    fullpage = html5 + htmlstart + head + content + htmlend
    return fullpage
sqlinj.run()
