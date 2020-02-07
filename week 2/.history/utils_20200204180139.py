import os.path
from os import path
from sys import argv
import python_second_assignment as myList

# A. first function takes a path to a folder and writes all filenames in the folder to a specified output file



lst=[]
def read_folder_recursive(folderpath):
    entries = os.listdir(folderpath)
    for entry in entries:
        if os.path.isdir(entry):
            read_folder_recursive(entry)
        else:
            lst.append(entry)

    myList.write_list_to_file('b_assignment.csv', lst)

read_folder_recursive(argv[1])
