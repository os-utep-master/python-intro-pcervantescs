# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:41:41 2019
@author: Paulina Cervantes
"""
import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists

if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]
    
#make sure text files exist
if not os.path.exists(textFname):
    print ("text file input %s doesn't exist! Exiting" % textFname)
    exit()

dictionary = {}

with open(textFname, 'r') as f:
    for word in f.read().split():
        word = word.lower()
        word = re.sub(r'[^\w\s]','',word)
        if word in dictionary.keys():
            value = dictionary.get(word) + 1
        else:
            value = 1
        dictionary[word] = value
  
with open(outputFname, 'w') as f:
    for key, value in sorted(dictionary.items()):
        print(key, value)
        f.write(key + ' ' + str(value) + '\n')   
