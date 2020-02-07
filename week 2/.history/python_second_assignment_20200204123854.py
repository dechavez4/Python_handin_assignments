# Exercise 1

# Create a python file with 3 functions:
#       A. def print_file_content(file) that can print content of a csv file to the console
import csv
from sys import argv
import platform

filename = argv[1]
def print_file_content(file):
    with open(filename) as csv_file:
        content = csv_file.readlines()
    
    for line in content[:20]:
        print(line.strip().split(','))

print_file_content(filename)

  #      B. def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
filename1 = argv[1]
def write_list_to_file(output_file, lst):
        if platform.system() == 'Windows':
            newline=''
        else:
            newline=None

    with open (output_file, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)

        write_list_to_file(filename1)

  #         rewrite the function so that it gets an arbitrary number of strings instead of a list
  #    def read_csv(input_file) that take a csv file and read each row into a list
  # Add a functionality so that the file can be called from cli with 2 arguments
  #    path to csv file
  #   an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.
  # Add a --help cli argument to describe how the module is used
