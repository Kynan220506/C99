import os
import shutil

source = input("Enter Source Folder Name: ")
destination = input("Enter Destination Folder Name: ")

source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file), destination)