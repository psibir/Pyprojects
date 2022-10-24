
import os

# insert directory to convert into folder variable
folder = ''
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    # replace first arg with current ext
    # replace second arg with desired ext
    newname = infilename.replace('.midi', '.mid')
    output = os.rename(infilename, newname)
