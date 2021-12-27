# مسِئول اموزش
from file_handler import *
import os


def check_college(a):
    c = 0
    college_list = ['electricity', 'mechanics', 'computer', 'math', 'physics', 'chemistry']
    for i in college_list:
        if i == a.lower():
            c += 1
    if c == 1:
        return True
    else:
        return False


# class Responsible_Training:         #ساخت درس، مشاهده پنل دانشجویان
#     def __init__(self,):

def create_lesson():
    while True:
        try:
            lesson_info = {}
            college = input('Enter college: ')
            if check_college(college):
                lesson_code = int(input('Enter lesson_code: '))
                lesson_name = input('Enter lesson name: ')
                professor_name = input('Enter professor name: ')
                unit_number = int(input('Enter unit number: '))
                capacity = int(input('Enter capacity: '))
                # lesson should pass
                prerequisite = input('Enter prerequisite(if does not exist enter no): ')
                new_pairs = [('id', lesson_code), ('college', college.capitalize()),
                             ('lesson_name', lesson_name.capitalize()),
                             ('professor_name', professor_name.capitalize()), ('unit_number', unit_number),
                             ('capacity', capacity), ('prerequisite', prerequisite.capitalize())]
                lesson_info.update(new_pairs)
                print(lesson_info)
                # lesson_name_unique = lesson_name + '.csv'
                os.chdir(r'colleges')
                # print(os.getcwdu())
                for i in ['electricity', 'mechanics', 'computer', 'math', 'physics', 'chemistry']:
                    if college.lower() == i:
                        f = i.capitalize() + '.csv'
                        lessons_file = FileHandler(f)
                        lessons_file.write_file(lesson_info)
                        return 'Lesson create successfully.'
                break
            else:
                print('Your college name is invalid! Try again.')
                continue
        except ValueError:
            print("Oops!  That was no valid input.  Try again...")


def view_student_list():
    # you want to see which of college
    s_list = FileHandler('students.csv')
    return s_list.read_file()


def view_student_panel():
    student_pass = input('Enter student password: ')
    student_fullname = student_pass.strip() + '.csv'
    if student_fullname in os.chdir(r'students'):
        s_f = FileHandler(student_fullname)
        print(s_f.read_file())
    else:
        print('This student does not exist')


# df.to_csv(os.path.join('myfolder', 'yourfilename.csv'))

print(create_lesson())
# print(view_student_panel())
# directory_of_python_script = os.path.dirname(os.path.abspath('Math'))
# df.to_csv(os.path.join(directory_of_python_script, 's.csv'))
# if field_of_study.capitalize() == 'Math':
#     lessons_file = FileHandler('Math.csv')
#     lessons_file.write_file(lesson_info)
# elif field_of_study.capitalize() == 'Physics':
#     lessons_file = FileHandler('Physics.csv')
#     lessons_file.write_file(lesson_info)
# elif field_of_study.capitalize() == 'Chemistry':
#     lessons_file = FileHandler('Chemistry.csv')
#     lessons_file.write_file(lesson_info)
# elif field_of_study.capitalize() == 'Computer':
#     lessons_file = FileHandler('Computer.csv')
#     lessons_file.write_file(lesson_info)
# elif field_of_study.capitalize() == 'Mechanics':
#     lessons_file = FileHandler('Mechanics.csv')
#     lessons_file.write_file(lesson_info)
# elif field_of_study.capitalize() == 'Electricity':
#     lessons_file = FileHandler('Electricity.csv')
#     lessons_file.write_file(lesson_info)
# else:
#     pass  # continue
# return lessons_file
