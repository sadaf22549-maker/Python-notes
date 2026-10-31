#organize folders

import os #os is used for working with files or folders
import shutil #shutil is used to copy,move or delete files or folders.

path=input("enter your path:")
files=os.listdir(path) #.listdir() is a method for os module which can list down the files from our given path.It returns a list of files.

for file in files:
    filename,extension=os.path.splitext(file)
    #.path.splitext() is another method which can divide the file into 2 pieces.one is file name & another one is extension.

    extension=extension[1:] #we used slicing to remove the dot(.) from extension

    if os.path.exists(path+"/"+extension):
        shutil.move(path+"/"+file,path+"/"+extension+"/"+file)

    else:
        os.makedirs(path+"/"+extension)
        shutil.move(path+"/"+file,path+"/"+extension+"/"+file)

    '''Here os.path.exists() checks the path is existed or not.if it is existed then shutil.move() will move the file from the source to destination

    path+"/"+file -->source path
    path+"/"+extension+"/"+file -->destination path
    
os.makedirs() -->makes a sub-folder if it isnt existed.then again shutil.move() do its work.
'''
    