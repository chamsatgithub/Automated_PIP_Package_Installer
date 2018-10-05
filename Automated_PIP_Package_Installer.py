#!/usr/bin/python
import os

file_input = raw_input("Enter the python file name:\n")
pkg_list = []
with open(file_input) as fi:
     lines = fi.readlines()
     for line in lines:
         if "import" in line:
             pkg_need_to_be_installed = line
             temp_pkg = line.split()
             for cand_pkg in temp_pkg:
                 if ',' in cand_pkg:
                     temp_cand_pkg = cand_pkg.split(',')
                     if type(temp_cand_pkg) is list:
                        for i in temp_cand_pkg:
                            if i is  '' or i is 'from' and i is 'import':
                               pass
                            else:
                               pkg_list.append(i)
                     else:
                        pkg_list.append(i)

                 elif '.' in cand_pkg:
                     temp_cand_pkg = cand_pkg.split('.')
                     if type(temp_cand_pkg) is list:
                        for i in temp_cand_pkg:
                            if i is  '' or i is 'from' and i is 'import':
                               pass
                            else:
                               pkg_list.append(i)
                     else:
                        pkg_list.append(i)
                 else:
                     temp_cand_pkg = cand_pkg
                     if type(temp_cand_pkg) is list:
                        for i in temp_cand_pkg:
                            if i is  '' or i is 'from' and i is 'import':
                               pass
                            else:
                               pkg_list.append(i)
                     elif temp_cand_pkg in 'from' and temp_cand_pkg in 'import':
                        pass
                     else:
                        pkg_list.append(temp_cand_pkg)
for i in pkg_list:
    if  i == 'from':
         pass 
    elif i == 'import':
         pass
    else:
         print("package need to be installed:",i)
         cmd_pip = "pip install {}".format(i)
         cmd_rsp = os.system(cmd_pip)





