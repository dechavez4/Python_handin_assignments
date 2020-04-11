from mypackage.classes.course import Course
from mypackage.classes.data_sheet import DataSheet
from mypackage.classes.student import Student
import sys
import random
import platform
import csv
import ast

print('__file__:{}\n__name__:{}\n__package__:{}\n'.format(__file__,__name__,str(__package__)))
lst_teachers = ["Elon Musk", "Steve Jobs", "Bill Gates"]
lst_names = ["Kurt Wonnegut", "Anne Hansen", "Peter Olsen", "Pia Nielsen", "Mette Pedersen"]
lst_course_names = ["Python", "JavaScript", "Java", "C++"]
lst_gender = ["Male", "Female"]
lst_grades = [0, 2, 4, 7, 10, 12]
lst_classrooms = [1.01, 1.62, 3.12]
lst_ETCS = [10, 20, 30]
lst_imgurl = ["img1", "img2", "img3"]

def rc(lst):
    return random.choice(lst)

def write_list_to_file(output_file, lst):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    
    with open(output_file, 'w', newline=newline) as output_file:

        fieldnames = ['NAME', 'GENDER', 'DATASHEET', 'IMG_URL']
        output_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        output_writer.writeheader()
        for line in lst:
            output_writer.writerow({'NAME' : line.name, 'GENDER' : line.gender,
             'DATASHEET' : line.data_sheet, 'IMG_URL' : line.image_url})


def generate_students(n):
    lst_students = []
    for i in range(n):
        lst_courses = [Course(rc(lst_course_names), rc(lst_classrooms), rc(lst_teachers), rc(lst_ETCS), rc(lst_grades)) for i in range(3)]
        new_dataSheet = DataSheet(lst_courses)
        lst_students.append(Student(rc(lst_names), rc(lst_gender), new_dataSheet, rc(lst_imgurl)))

    write_list_to_file('students.csv', lst_students)

def read_csv():
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    with open('students.csv', newline=newline) as f:
        reader = csv.reader(f)
            #for l in row:
            #    print("---------------", l)
            #my_list.append(Student(row[0], row[1], Course(row[2]), row[3]))

        my_list = list(reader)
        #print(my_list)
    grades = []
    sum = 0
    for student in my_list[1:]:
        currData = DataSheet(student[2])
 
        literal = ast.literal_eval(currData.courses)

        for l in literal:
            grades.append(l[4])
            sum += l[4];
        
        print("GRADES: ",grades)
        print("AVG GRADE: ",sum/len(grades))
    
            

        
    return my_list

def print_students():
    students = []

    for student in read_csv()[1:]:
        students.append({'name': student[0], 'gender' : student[1], 'courses' : student[2], 'img_url': student[3]})
    return students

def print_grades():
    grades = []

    for student in read_csv()[1:]:
        for grade in student[2]:
            grades.append({'grade': grade})

    return grades

if __name__ == "__main__":
    print("Hello in demo")
    generate_students(4)
   # print("----------",print_grades())
    print("Print_Students: ",print_students())