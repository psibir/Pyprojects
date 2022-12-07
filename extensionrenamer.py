
import os

folder = input("Enter the absolute path of the directory containing files you wish to be changed: ")
old_ext = input("Enter the previous file extension: ").removeprefix(".")
new_ext = input("Enter the new file extension:  ").removeprefix(".")

for filename in os.listdir(folder):
    oldfilename = os.path.join(folder, filename)
    if not os.path.isfile(oldfilename): continue
    oldbase = os.path.splitext(filename)
    if not old_ext == oldbase[1].removeprefix("."): continue
    newname = (oldbase[0]+"."+new_ext)   
    newfilename = os.path.join(folder,newname)

    output = os.rename(oldfilename, newfilename)
