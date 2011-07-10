#!/usr/bin/python
#-*- coding=utf-8 -*-

import sys
import os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + "/src")
print sys.path

from mysqlhelper import *

def print_hello(): 
    print """Please select job for continue
    1. Create new mail user
    2. Change password for existing user
    """
    choice = raw_input()
    return choice

def getmaneandpass():
    print """Please enter user name 
    (example: someusername)
    without any  @
    """
    usname = raw_input()
    print """Please enter user password"""
    uspassword = raw_input()
    return (usname, uspassword)

def add_modyfy_user(sql, cursor):
    db.cursor.execute(sql)
    db.cursor.close()
    db.commit()
"""
Main program
"""
db = mysqlhelper('localhost', 'root', '', 'mail')
a = str(print_hello())

if (a == "1"):
    print "You are deside to create new mail user"
    params = getmaneandpass()
    sql="INSERT INTO virtual_users (domain_id,user,password,passplain) VALUES (2,\"%s\",PASSWORD(\"%s\"),\"%s\")" % (params[0], params[1], params[1])
    add_modyfy_user(sql, db)
elif (a == "2"):
    print "You are deside to change user password \n"
    params = getmaneandpass()
    sql="UPDATE virtual_users SET passplain=\"%s\", password=PASSWORD(\"%s\") WHERE user=\"%s\"" % (params[1], params[1], params[0])
    print sql;
    add_modyfy_user(sql, db)

#print sql
#db.mhprintresult('virtual_users', '1=1')
