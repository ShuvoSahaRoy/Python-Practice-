import os
from datetime import datetime

# current working directory
print(os.getcwdb())

# change working directory
# os.chdir('E:/codes/')
# print(os.getcwdb())

# list of directory on current working folder
# print(os.listdir())

# create directory and subdirectory
# os.makedirs("directory name/subdirectory")

# remove directory if there are no sub directory
# os.rmdir("directory name")

# remove with sub directory
# os.removedirs("directory name/sub directory")

# folder rename doesn't work like that. it's for any file
# os.rename("directory name", "new folder")
# os.rename("check.py", "for check.py")

# print details of a file
# print(os.stat("for check.py"))
# print(os.stat("for check.py").st_size)  # return result in bytes

# modification_time = os.stat("for check.py").st_mtime
# print(datetime.fromtimestamp(modification_time))  # in readable format


# to get all path, directories and all files name
for dirpath, dirnames, filenames in os.walk(os.getcwdb()):
    print('Current path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

BASE_DIR = os.getcwd()
print(os.path.join(BASE_DIR, 'new_file.txt'))
