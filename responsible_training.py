# مسِئول اموزش
from file_handler import *
import os
import log


def check_college_rt(a):
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
            if check_college_rt(college):
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
                        log.info_logger.info('Lesson create successfully.')
                        return 'Lesson create successfully.'
                break
            else:
                print('Your college name is invalid! Try again.')
                continue
        except ValueError as e:
            log.warning_logger.error(f'{e}')
            print("Oops!  That was no valid input.  Try again...")


def view_student_list():
    # you want to see which of college
    s_list = FileHandler('students_list.csv')
    return s_list.read_file()


def view_student_panel():
    while True:
        try:
            student_pass = input('Enter student password: ')
            student_fullname = student_pass.strip()
            os.chdir(r"C:\Users\Admin\Desktop\maktab65\tamarin python\پروژه پایتون\maktab_python_project_elahe")
            file_m = FileHandler("students_list.csv")
            if file_m.check_unique_id(student_fullname):
                os.chdir(r"C:\Users\Admin\Desktop\maktab65\tamarin python\پروژه پایتون"
                         r"\maktab_python_project_elahe\students")
                os.chdir(student_fullname)
                print(os.getcwd())
                s_info = FileHandler('information.csv')
                s_r = s_info.read_file()
                college = s_r[0]['college'].capitalize()
                s_f = FileHandler(student_fullname + '.csv')
                print(s_f.read_file())
                rt_opinion = int(input("1)Accept courses\n2)Deny courses\nEnter: "))
                if rt_opinion == 1:
                    log.info_logger.info("Responsible training accept courses.")
                    return "courses accepted."
                elif rt_opinion == 2:
                    deny_c = int(input("Enter cod of course:"))
                    if s_f.check_unique_id(deny_c):
                        s_f.delete_row(deny_c)
                        os.chdir(r"C:\Users\Admin\Desktop\maktab65\tamarin python\پروژه پایتون"
                                 r"\maktab_python_project_elahe\colleges")
                        course_f = FileHandler(college + '.csv')
                        all_rows = course_f.read_file()
                        for row in all_rows:
                            if row["id"] == str(deny_c):
                                q = int(row["capacity"])
                                row["capacity"] = str(q + 1)
                                print(row)
                                course_f.edit_row(row)
                                log.info_logger.info("Responsible training deny course.")
                                return "course deleted."
                    else:
                        print('Code is invalid!')
                        continue
                else:
                    print('Enter 1 or 2')
                    continue
            else:
                print('This student does not exist')
                continue
        except Exception as c:
            log.warning_logger.error(f'{c}')
            print(c)


# df.to_csv(os.path.join('myfolder', 'yourfilename.csv'))

# print(create_lesson())
print(view_student_panel())
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
