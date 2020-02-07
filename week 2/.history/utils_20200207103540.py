import os.path
from os import path
from sys import argv
import argparse

import python_second_assignment as myList

# 1. first function takes a path to a folder and writes all filenames in the folder to a specified output file
folderpath = "/Users/robin/Desktop/semester_4/python/myPythonCode/week 2"
def read_folder(foldername, filename):
    myList.write_list_to_file(filename, os.listdir())
read_folder(argv[1], argv[2])

#2.second takes a path to a folder and write all filenames recursively (files of all sub folders to)
lst=[]
def read_folder_recursive(folderpath):
    entries = os.listdir(folderpath)
    for entry in entries:
        if os.path.isdir(entry):
            read_folder_recursive(entry)
        else:
            lst.append(entry)

    myList.write_list_to_file(argv[2], lst)

read_folder_recursive(argv[1])

# 3. third takes a list of filenames and print the first line of each
def read_first_line_from_files(*files):
    for file in files:
        for ele in file:
            with open(ele) as f_obj:
                content = f_obj.readline()
                print(content)

def run():
    if args.exercise_2_1:
        read_folder(argv[2], argv[3])
    if args.exercise_2_2:
        read_folder_recursive(argv[2])
    if args.exercise_2_3:
        read_first_line_from_files(argv[2])
    if args.file:
        if path.exists(argv[2]):
            read_folder(argv[2], argv[3:])
        else:
            print("file doesnt exist", argv[2])    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="------------------Assignments 2---------------------")
    parser.add_argument("--exercise_2_1", help='first function takes a path to a folder and writes all filenames in the folder to a specified output file')
    parser.add_argument("--exercise_2_2", nargs="*", help="second takes a path to a folder and write all filenames recursively (files of all sub folders to).")
    parser.add_argument("--exercise_2_3", nargs="*", help="third takes a list of filenames and print the first line of each.")
    args = parser.parse_args()
    run()