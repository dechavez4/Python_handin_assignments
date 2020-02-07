import os.path
from os import path
from sys import argv
import python_second_assignment as myList

# A. first function takes a path to a folder and writes all filenames in the folder to a specified output file
folderpath = "/Users/robin/Desktop/semester_4/python/myPythonCode/week 2"
def read_folder():
    entries = os.listdir(folderpath)
    for entry in entries:
        print(entry)
myList.write_list_to_file(argv[2])