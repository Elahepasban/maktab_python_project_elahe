from file_handler import *
import os
import csv
import log


class Student:
    def __init__(self, password):
        self.info = []
        self.password = password
        self.list_selectable_courses = []
        self.list_passed = []
        self.units = 0
        self.college = " "
        self.files = FileHandler(self.password + '.csv')

    def view_student_info(self):
        os.chdir(r"C:\Users\Admin\Desktop\maktab65\tamarin python\پروژه پایتون"
                 r"\maktab_python_project_elahe - Copy\students")
        os.chdir(self.password)
        student_info = FileHandler('information.csv')
        cop = student_info.read_file().copy()
        del cop[0]["id"]
        self.info = cop
        self.college = self.info[0]['college'].capitalize()
        # with open(self.password + '.csv', newline='') as cs:
        read = self.files.read_file()
        num = 0
        for row in read:
            for j in self.list_passed:
                if j != row['lesson_name']:
                    num += 1
            if num == len(self.list_passed):
                self.list_passed.append(row['lesson_name'])
        return self.info

    def view_courses_list(self):
        self.view_student_info()
        os.chdir(r"C:\Users\Admin\Desktop\maktab65\tamarin python\پروژه پایتون"
                 r"\maktab_python_project_elahe - Copy\colleges")
        with open(self.college + '.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['prerequisite'] == 'No':
                    print(row)
                else:
                    for i in self.list_passed:
                        if i == row['prerequisite']:
                            print(row)
            return " "

    def select_courses(self):
        n1 = 0
        n2 = 0
        self.view_student_info()
        while self.units < 21:
            try:
                units = self.files
                q = units.read_file()
                for i in q:
                    self.units += int(i['unit_number'])
                select = int(input('Enter code of the course that you want(exit = enter 0): '))
                if select == 0 and self.units > 9:
                    break
                elif select == 0 and self.units < 10:
                    print("Your units is less than 9. You should select more courses!")
                    continue
                elif select != 0:
                    if self.files.check_unique_id(select):
                        print('You select this course later. Select new course')
                        continue
                    else:
                        os.chdir(
                            r"C:\Users\Admin\Desktop\maktab65\tamarin python\پروژه پایتون"
                            r"\maktab_python_project_elahe - Copy\colleges")
                        k = FileHandler(self.college + '.csv')
                        all_rows = k.read_file()
                        for row in all_rows:
                            if row["id"] == str(select):
                                n1 += 1
                                q = int(row["capacity"])
                                if q > 0:
                                    n2 += 1
                                    row["capacity"] = str(q - 1)
                                    print(row)
                                    k.edit_row(row)
                                    os.chdir(
                                        r"C:\Users\Admin\Desktop\maktab65\tamarin python\پروژه پایتون"
                                        r"\maktab_python_project_elahe - Copy\students")
                                    os.chdir(self.password)
                                    row['score'] = 0
                                    print(self.files.write_file(row), 'select courses successfully')
                                    log.info_logger.info('select courses successfully')
                                    continue
                        if n1 == 0:
                            print("This code is invalid!")
                            continue
                        if n2 == 0:
                            print("The capacity is full!")
                            continue
                return " "
            except ValueError as e:
                print(f'{e} try again.')
                log.warning_logger.error(f'{e}')
            # except TypeError as z:
            #     print(f'{z} try again.')

    def view_courses_select(self):
        units = self.files
        q = units.read_file()
        for i in q:
            self.units += int(i['unit_number'])
        print(f'Yor units:{self.units}\nyour courses selected is:\n{self.files.read_file()}')
        return ''

# if __name__ == '__main__':
#     print(__name__)

# a = Student('1382696')
# print(a.view_student_info())
# print(a.college)
# print(a.view_courses_select())
# print(a.view_courses_list())
# print(a.list_passed)
# print(a.select_courses())
# print(a.units)
# print(a.manage_unit(1001))
# print(a.view_courses_select())
# def view_courses_list(self):
#     list_passed = []
#     # courses_permissible = []
#     # os.chdir(r"students")
#     # os.chdir(self.s_password)
#     self.courses = FileHandler(self.s_password + '.csv')
#     l = self.courses.read_file()
#     for i in l:
#         list_passed.append(i["lesson_name"])
#     os.chdir(r"C:\Users\Admin\Desktop\maktab65\tamarin python\پروژه پایتون\maktab_python_project_elahe\colleges")
#     self.college = self.info[0]["college"].capitalize() + ".csv"
#     with open(self.college, 'r') as read_obj:
#         csv_dict_reader = DictReader(read_obj)
#         for row in csv_dict_reader:
#             # row variable is a dictionary that represents a row in csv
#             # if row["prerequisite"] in list_passed:
#             for j in list_passed:
#                 if row["prerequisite"] == j or row["prerequisite"] == 'no':
#                     self.courses_permissible.append(row)
#                     return self.courses_permissible
#                 else:
#                     print('There is no lesson yet.It could be because of you do not pass prerequisites!')
# def select_courses(self):
#     courses_select_l = []
#     print(f'Your list of courses:\n')
#     for i in self.courses_permissible:
#         print(i)
#     while True:
#         try:
#             select = int(input('Enter code of the course that you want(exit = enter 0): '))
#             if select == 0:
#                 break
#             else:
#                 for j in self.courses_permissible:
#                     if j["id"] == select:
#                         if j['capacity'] > 0:
#                             self.courses.write_file(j)
#                             j['capacity'] -= 1
#                             os.chdir(r"colleges")
#                             courses_capacity = FileHandler(self.courses)
#                             courses_capacity.edit_row(j)
#                             courses_select_l.append(j)
#                             return courses_select_l
#     if i['id'] == select:
#         num2 += 1
#         if i['capacity'] > 0:

#             num3 += 1
# if num2 == 0:
#     print("This code is invalid")
#     continue
# elif num2 > 0 and num3 == 0:
#     print("The capacity is full!")
#     continue
# else:
#     print('Select course successfully.')
# os.chdir(r"C:\Users\Admin\Desktop\maktab65\tamarin python\پروژه پایتون\maktab_python_project_elahe\colleges")
# file_n = self.info[0]["college"].capitalize() + '.csv'
# file = FileHandler(file_n)
# file_r = file.read_file()
# for i in file_r:
#     if i['id'] == select and i['capacity'] > 0:
#         i['capacity'] -= 1
#         file.edit_row(i)
#         os.chdir(r"students")
#         os.chdir(self.password)
#         files = FileHandler(self.password + '.csv')
#         i['score'] = 0
#         files.write_file(i)
#         self.units += i['unit_number']
#         print('Select course successfully.')
#         # num2 += 1
