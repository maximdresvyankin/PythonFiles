#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os.path
import re

# def findall(path):
if (len(sys.argv)>1): path=sys.argv[1]
else: path=raw_input("Введите директорию поиска \n")
while (path==""):
    print "Введите существующую директорию поиска"
    path=raw_input()
    if not(os.path.exists(path)): path=""
    else: print "Path %s exist \n" % path

print "#"*40
#print "%s" % path
listoffiles = []
for names in os.walk(path):
    for files in names[2]:
        counter = 0
        if (re.search('(.cue$)', files) and not(re.search('(.cueuft.cue)', files))): 
            listoffiles.append(os.path.join(names[0], files))
for all in listoffiles:
     preall=all.split(".")[0]
     print "\"%s\" \t \"%s\"" % (all, preall+".utf.cue")
     #os.system( "iconv -f CP1251 -t UTF-8 \"%s\" > \"%s\"" % (all, all+".utf.cue"))
    
#iconvpath=os.system('/usr/bin/iconv')
#print iconvpath
