

import os

folder = input("What is the absolute path of the directory? ")
old_ext = input("What is the previous file extension? ").removeprefix(".")
new_ext = input("What would you like to change the extension to? ").removeprefix(".")

for filename in os.listdir(folder):
    oldfilename = os.path.join(folder, filename)
    if not os.path.isfile(oldfilename): continue
    oldbase = os.path.splitext(filename)
    if not old_ext == oldbase[1].removeprefix("."): continue
    newname = (oldbase[0]+"."+new_ext)   
    newfilename = os.path.join(folder,newname)

    output = os.rename(oldfilename, newfilename)
