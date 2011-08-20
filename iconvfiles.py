#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os
import re
from chardet.universaldetector import UniversalDetector

def detectcharset(filename):
    #Function for detect file charset
    detector = UniversalDetector()
    detector.reset()
    for line in file(filename, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    return(detector.result)

# Param checks.    
if (len(sys.argv) > 1): path = sys.argv[1]
else: path = raw_input("Введите директорию поиска \n")
while not(os.path.exists(path)):
    print "Введите существующую директорию поиска"
    path = raw_input()

# Begin program
print "#" * 40
print("Start")
listoffiles = []
counter = 0
for names in os.walk(path):
    for files in names[2]:
        if (re.search('(cue$)', files) and not(re.search('(utf.cue)', files))): 
            listoffiles.append(os.path.join(names[0], files))
counter = 0
lenoflist = len(listoffiles)
for all in listoffiles:
     try:
         inpenc = detectcharset(all)['encoding'].upper()
         counter += (100.0 / lenoflist)
         sys.stdout.write("{0:-6.2f}% \t".format(counter))
         print all
         os.system("iconv -f {0} -t UTF-8 \"{1}\" > \"{2}\"".format(inpenc, all, ".tmpfile"))
         tempfile = open(".tmpfile", "r")
         newfile = open(all[:-3] + "utf.cue", "w")
         newfile.write(tempfile.read())
         newfile.close()
         tempfile.close()
         os.system("rm -rf .tmpfile")
     except :
         print('Error!!!')
         sys.exit (1)
print("Complete")
print("#"*40)