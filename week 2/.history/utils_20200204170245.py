import os.path
from os import path
from sys import argv

# A. first function takes a path to a folder and writes all filenames in the folder to a specified output file
def read_folder():
    with open(argv[1], 'w') as f:
    data = 'some data to be written to the file'
    f.write(data)


