import os.path
from os import path
from sys import argv
import python_second_assignment as myList

# A. first function takes a path to a folder and writes all filenames in the folder to a specified output file
def read_folder():
    entries = os.listdir('myPythonCode')
    for entry in entries:
        print(entry)
read_folder()