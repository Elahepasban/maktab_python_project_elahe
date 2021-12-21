# مسِئول اموزش
import csv
from file_handler import *
import pandas as pd
import os.path


# class Responsible_Training:         #ساخت درس، مشاهده پنل دانشجویان
#     def __init__(self,):
#
#
def create_lesson():
    # while True
    lesson_info = {}
    lesson_code = int(input('Enter lesson_code: '))
    field_of_study = input('Enter lesson field of study: ')
    lesson_name = input('Enter lesson name: ')
    professor_name = input('Enter professor name: ')
    unit_number = input('Enter unit number: ')
    capacity = input('Enter capacity: ')
    prerequisite = input('Enter prerequisite: ')  # lesson should pass
    new_pairs = [('id', lesson_code), ('field_of_study', field_of_study.capitalize()),
                 ('lesson_name', lesson_name.capitalize()),
                 ('professor_name', professor_name.capitalize()), ('unit_number', unit_number.capitalize()),
                 ('capacity', capacity.capitalize()), ('prerequisite', prerequisite.capitalize())]
    lesson_info.update(new_pairs)
    # lesson_name_unique = lesson_name + '.csv'
    if field_of_study.capitalize() == 'Math':
        lessons_file = FileHandler('Math.csv')
        lessons_file.write_file(lesson_info)
    elif field_of_study.capitalize() == 'Physics':
        lessons_file = FileHandler('Physics.csv')
        lessons_file.write_file(lesson_info)
    elif field_of_study.capitalize() == 'Chemistry':
        lessons_file = FileHandler('Chemistry.csv')
        lessons_file.write_file(lesson_info)
    elif field_of_study.capitalize() == 'Computer':
        lessons_file = FileHandler('Computer.csv')
        lessons_file.write_file(lesson_info)
    elif field_of_study.capitalize() == 'Mechanics':
        lessons_file = FileHandler('Mechanics.csv')
        lessons_file.write_file(lesson_info)
    elif field_of_study.capitalize() == 'Electricity':
        lessons_file = FileHandler('Electricity.csv')
        lessons_file.write_file(lesson_info)
    else:
        pass  # continue
    return lessons_file

    print('Lesson create successfully.')
    return lesson_file


def view_student_list():
    pass


def view_student_panel(student_name):
    pass


# df.to_csv(os.path.join('myfolder', 'yourfilename.csv'))
a = create_lesson()
print(a[0])
print(a[2])
l = a[2]
p = a[0] + '.csv'
print(p)
lesson_file = FileHandler(p)
lesson_file.write_file(l)
import os

# directory_of_python_script = os.path.dirname(os.path.abspath('Math'))
# df.to_csv(os.path.join(directory_of_python_script, 's.csv'))
