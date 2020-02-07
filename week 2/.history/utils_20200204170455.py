import os.path
from os import path
from sys import argv

# A. first function takes a path to a folder and writes all filenames in the folder to a specified output file
entries = os.listdir('myPythonCode/')
def read_folder():
    with open(, 'w') as f:
        data = 'some data to be written to the file'
        f.write(data)
read_folder()

