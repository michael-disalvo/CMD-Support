# this file is a test of the OS module
import os

# print current working directory
currentWorkingDirectory = os.getcwd()

# change directroy
# os.chdir('/Users/micha')

# Create a list of what files and folders are in cwd
cwd_content = os.listdir()
# or pass a path into listdir() to get files and folders from another directory

# create a new folder
folder_name = (
    "sample_folder/second_folder"  # would create another folder inside the folder
)
# os.mkdir(file_name)

# delete folder
# os.rmdir(foldername)
# o.removedirs(foldername) #does delete recursively (can be dangerous)

# rename file/folder
# os.rename(original_name, new_name)

# get information about a file
# os.stat(filename)
# returns infomration like size and time of last modification
# import datetime from datetime and the function .fromtimestap(time) will put the time into a human readable form

# see entire directory tree
# traverses the hole file system starting at the argument you pass three value tuples
for dirpath, dirnames, filenames in os.walk("/Users/micha/VS Code Projects"):
    print("Current path: ", dirpath)
    print("Current Directorys: ", dirnames)
    print("files: ", filenames)


# working with os.path

# os.path.join() will properly join two paths together

end_of_path = os.path.basename("/micha/ClionProjects")  # gives the ending of the path



parts = os.path.split(os.getcwd())  # returns a tuple: (path, basename)

x = os.path.exists("/path/file")  # checks if a path exists

# os.path.isfile(..) or os.path.isdir(..)

second_split = os.path.splitext("/OSTest.py")  # splits root of path and extension
print(second_split)
