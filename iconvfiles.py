#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os
import re
from chardet.universaldetector import UniversalDetector 

def detectcharset(filename):
    detector = UniversalDetector()
    detector.reset()
    for line in file(filename, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    return(detector.result)
    
# def findall(path):
if (len(sys.argv) > 1): path = sys.argv[1]
else: path = raw_input("Введите директорию поиска \n")
while (path == ""):
    print "Введите существующую директорию поиска"
    path = raw_input()
    if not(os.path.exists(path)): path = ""
    else: print "Path %s exist \n" % path

print "#" * 40
print("Start")
#print "%s" % path
listoffiles = []
counter = 0
for names in os.walk(path):
    for files in names[2]:
        if (re.search('(cue$)', files) and not(re.search('(utf.cue)', files))): 
            listoffiles.append(os.path.join(names[0], files))
counter = 0
lenoflist = len(listoffiles)
for all in listoffiles:
#     print "\"%s\" \t \"%s\"" % (all, preall + "utf.cue")
     try:
         inpenc=detectcharset(all)['encoding'].upper()
         os.system("iconv -f {0} -t UTF-8 \"{1}\" > \"{2}\"".format(inpenc,all,all[:-3] + "utf.cue"))
         counter+=100/lenoflist
         sys.stdout.write("{0:-3d}%".format(counter))
     except os.error, e:
         print('Error {0} : {1}'.format(e.args[0], e.args[1]))
         sys.exit (1)
print("Complete")
print("#"*40)    
#iconvpath=os.system('/usr/bin/iconv')
#print iconvpath