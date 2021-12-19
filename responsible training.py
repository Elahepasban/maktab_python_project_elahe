import csv
from file_handler import *


# class Responsible_Training:         #ساخت درس، مشاهده پنل دانشجویان
#     def __init__(self,):
#
#
def create_lesson():
    lesson_info = {}
    lesson_name = input('Enter lesson name: ')
    professor_name = input('Enter professor name: ')
    unit_number = input('Enter unit number: ')
    capacity = input('Enter capacity: ')
    prerequisite = input('Enter prerequisite: ')  # lesson should pass
    new_pairs = [('lesson_name', lesson_name.capitalize()), ('professor_name', professor_name.capitalize()),
                 ('unit_number', unit_number.capitalize()),
                 ('capacity', capacity.capitalize()), ('prerequisite', prerequisite.capitalize())]
    lesson_info.update(new_pairs)
    lesson_name_unique = lesson_name + '.csv'
    with open(lesson_name_unique, 'w', newline='') as lesson_name_unique:
        writer = csv.writer(lesson_name_unique)
        writer.writerow(['lesson_name', 'professor_name', 'unit_number', 'capacity', 'prerequisite'])
    lesson_file = FileHandler(lesson_name + '.csv')
    lesson_file.write_file(lesson_info)
    print('Lesson create successfully. Now check it.',lesson_file.read_file())

def view_student_list():
    pass


def view_student_panel(student_name):
    pass


a = create_lesson()
print(a)
