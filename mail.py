#!/usr/bin/python
#-*- coding=utf-8 -*-

import sys
import os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + "/src")
from mysqlhelper import *

def print_hello(): 
    print("""Please select job for continue
    1. Create new mail user
    2. Change password for existing user
    3. Show user info
    """)
    choice = raw_input()
    return choice

def getmaneandpass():
    print("""Please enter user name 
    (example: someusername)
    without any  @
    """)
    usname = raw_input()
    print("Please enter user password")
    uspassword = raw_input()
    return (usname, uspassword)

def mainprogramm():
    db = mysqlhelper('localhost', 'root', '', 'mail')
    a = str(print_hello())

    if (a == "1"):
        print("You are deside to create new mail user")
        params = getmaneandpass()
        sql = "INSERT INTO virtual_users (domain_id,user,password,passplain) VALUES (2,\"%s\",PASSWORD(\"%s\"),\"%s\")" % (params[0], params[1], params[1])
        db.mhsqlrun(sql)
    elif (a == "2"):
        print("You are deside to change user password \n")
        params = getmaneandpass()
        sql = "UPDATE virtual_users SET passplain=\"%s\", password=PASSWORD(\"%s\") WHERE user=\"%s\"" % (params[1], params[1], params[0])
        print(sql);
        db.mhsqlrun(sql)
    elif (a == "3"):
        print("Please type username without \@")
        username = raw_input()
        sql = "SELECT * FROM virtual_users WHERE user=\"%s\""
        a = db.mhfetchrow("virtual_users", "user=\"%s\"" % username)
        fealdlist = ('id', 'Mail Domain id', 'User Name', 'Hash Password', 'Plain Password')
        print("Details for user " + a[0][2])
        for i in range(0, len(a[0])):
            print('{0:<25} => {1:<100}'.format(fealdlist[i],str(a[0][i])))
            
    print("Do you want another task to do? Y/N")
    again = str(raw_input()).lower()
    print(again)
    if again == "y":
        mainprogramm()
    elif again == "n":
        sys.exit(0)
"""
Main program
"""
mainprogramm()