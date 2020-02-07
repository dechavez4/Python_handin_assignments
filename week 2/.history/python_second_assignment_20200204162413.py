# Exercise 1

# Create a python file with 3 functions:
#       A. def print_file_content(file) that can print content of a csv file to the console
import csv
from sys import argv
import platform
import argparse

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

def run():
    if args.exercise1:
        print_file_content(argv[2])
    if args.exercise2:
        inputfield = argv[3:]
        write_list_to_file(argv[@], inputfield)    
    if args.exercise3:
        read_line(argv[2])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--print", help='function that can print content of a csv file to the console')
    parser.add_argument("--write", nargs="*", help='function that can take a list of tuple and write each element to a new line in file')
    parser.add_argument("--read", help='function that take a csv file and read each row into a list')
    args = parser.parse_args()
    run()