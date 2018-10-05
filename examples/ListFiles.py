#!/usr/bin/python

import os, glob

Dir_Name = raw_input("Please enter the directory path to list the file/Dir names: ")

dirs_files = glob.glob('{}/*'.format(Dir_Name))

print("Here is the list of Dirs and Files:\n",dirs_files)



