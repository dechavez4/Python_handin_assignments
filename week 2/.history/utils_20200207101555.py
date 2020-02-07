import os.path
from os import path
from sys import argv
import python_second_assignment as myList

# A. first function takes a path to a folder and writes all filenames in the folder to a specified output file

#folderpath = "/Users/robin/Desktop/semester_4/python/myPythonCode/week 2"
#def read_folder(foldername, filename):
#    myList.write_list_to_file(filename, os.listdir())
#read_folder(argv[1], argv[2])

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
def read_first_line(*files):
    with open(files) as file_object:
        content = file_object.readline()
        print(content)
    for line in content:
        print(line.rstrip())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="------------------Assignments 2---------------------")
    parser.add_argument("--print", help='function that can print content of a csv file to the console')
    parser.add_argument("--write", nargs="*", help='function that can take a list of tuple and write each element to a new line in file')
    parser.add_argument("--read", help='function that take a csv file and read each row into a list')
    parser.add_argument("--file", nargs="*", help="an argument that if given will write the content to file_name or otherwise will print it to the console.")
    args = parser.parse_args()
    run()