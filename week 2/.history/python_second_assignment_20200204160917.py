# Exercise 1

# Create a python file with 3 functions:
#       A. def print_file_content(file) that can print content of a csv file to the console
import csv
from sys import argv
import platform
import argparse
filename = argv[1]
def print_file_content(file):
    with open(filename) as csv_file:
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

def main():
    if argv[2] == 'exercise1':
        print_file_content(filename)
    if argv[2] == 'write_list_to_file':
        inputfield = argv[3:]
        write_list_to_file(filename, inputfield)    
    if argv[2] == 'read_line':
        read_line(filename)


def run():


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--exercise1", help='print a file')
    
    print(parser)