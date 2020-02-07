import os.path
from os import path
from sys import argv

# A. first function takes a path to a folder and writes all filenames in the folder to a specified output file
entries = os.listdir('.../myPythonCode/')
def read_folder():
    with os.scandir('entries') as f:
        for entry in f:
            print(entry.name)
read_folder()
