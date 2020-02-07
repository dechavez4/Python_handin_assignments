import csv
from sys import argv
import platform
import argparse
import os.path
from os import path
# Create a python file with 3 functions:
#       A. def print_file_content(file) that can print content of a csv file to the console
def print_file_content(file):
    with open(file) as csv_file:
        content = csv_file.readlines()
    
    for line in content[:20]:
        print(line.strip().split(','))

# kan overskrive den gamle file. 
  #      B. def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
def write_list_to_file(output_file, *lst):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None

    with open (output_file, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        for ele in lst:
            output_writer.writerow(ele)


  # C.    def read_csv(input_file) that take a csv file and read each row into a list

def read_line(file):
    with open(file) as file_object:
        lines = file_object.readlines()
        print(lines)
    for line in lines:
        print(line.rstrip()) 


# 2. Add a functionality so that the file can be called from cli with 2 arguments
def run():
    if args.print:
        print_file_content(argv[2])
    if args.write:
        write_list_to_file(argv[2], argv[3:])    
    if args.read:
        read_line(argv[2])
    #if args.file:
     #   path.exists(argv[2])
     #   write_list_to_file(argv[2], argv[3:])
    #else:
     #   print("file doesnt exist", argv[2])    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="this is my menu")
    parser.add_argument("--print", help='function that can print content of a csv file to the console')
    parser.add_argument("--write", nargs="*", help='function that can take a list of tuple and write each element to a new line in file')
    parser.add_argument("--read", help='function that take a csv file and read each row into a list')
   # parser.add_argument("--file", nargs="*", help="an argument that if given will write the content to file_name or otherwise will print it to the console.")
    args = parser.parse_args()
    run()