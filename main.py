import time
import log
import hashlib
import register
from file_handler import *
import os
from csv import DictReader
import Responsible_Training
import student


def cls():
    print("\n" * 15)


def encode(u, p):
    b = u + p
    # encode it to bytes using UTF-8 encoding
    message = b.encode()
    i = hashlib.blake2s(message).hexdigest()
    return i


def get_info(file):
    counter = 0
    while counter < 3:
        username = input("Enter your username and password please.\nusername(7character): ")
        password = input('\npassword(7character): ')
        k_id = encode(username, password)
        k = FileHandler(file)
        if k.check_unique_id(k_id):
            # log.info_logger.info('User login successfully.')
            return True
        n = input('Your username or password is invalid! Do you want try again?(y,n): ')
        if n == 'y':
            counter += 1
            continue
        else:
            return False
    else:
        print('Your account lock for 5 seconds.')
        time.sleep(5)
        log.info_logger.error('User responsible_trainings login failed.')
        return False


# text = ..
# text.expandtabs(10)
def menu():
    while True:
        entrance_user = input("Welcome to unit selection system of Science college\nChoose from the following options"
                              "\n\n1)Responsible_Training\t\t\t2)Student\t\t\t3)Register\t\t\t4)Exit\n\nEnter: ")
        try:
            if entrance_user == '1':
                p = get_info('responsible_trainings.csv')
                if p == True:
                    log.info_logger.info('User responsible training login.')
                    print('Welcome to your panel.')
                    while True:
                        rt_menu = int(input("1)Create lesson\n2)View student list\n3)View student panel\n4)Exit\nNumber: "))
                        cls()
                        if rt_menu == 1:
                            print(Responsible_Training.create_lesson())
                            a2 = input("1)Continue\n2)Exit")
                            if a2 == '1':
                                continue
                            else:
                                break
                        elif rt_menu == 2:
                            print(Responsible_Training.view_student_list())
                            a2 = input("1)Continue\n2)Exit")
                            if a2 == '1':
                                continue
                            else:
                                break
                        elif rt_menu == 3:
                            print(Responsible_Training.view_student_panel())
                            a2 = input("1)Continue\n2)Exit")
                            if a2 == '1':
                                continue
                            else:
                                break
                        elif rt_menu == 4:
                            break
                        else:
                            print('invalid number!')
                            continue
                else:
                    # log.warning_logger.error(f"User responsible training doesn't exist.")
                    # print("Your username or password is invalid! try again.")
                    continue
            elif entrance_user == '2':
                os.chdir(r"C:\Users\Admin\Desktop\maktab65\tamarin python\پروژه پایتون"
                         r"\maktab_python_project_elahe - Copy\students")
                co = 0
                while co < 3:
                    username_s = input("Enter your username and password please.\nusername(7character): ")
                    password_s = input('\npassword(7character): ')
                    c = password_s.strip()
                    os.chdir(c)
                    f_id = encode(username_s, password_s)
                    f = FileHandler('information.csv')
                    if f.check_unique_id(f_id):
                        log.info_logger.info('User student login.')
                        cls()
                        with open('information.csv', 'r') as read_obj:
                            # pass the file object to DictReader() to get the DictReader object
                            csv_dict_reader = DictReader(read_obj)
                            for row in csv_dict_reader:
                                print(
                                    f'Hi {row["firstname"].capitalize()} {row["lastname"].capitalize()}.'
                                    f' Welcome to your panel.')
                        while True:
                            s_menu = int(input('1)View my information\n2)View courses list\n3)Select courses\n4)'
                                               'view courses selected\n5)Exit\nNumber: '))
                            student_ob = student.Student(c)
                            if s_menu == 1:
                                print(student_ob.view_student_info())
                                a2 = input("1)Continue\n2)Exit")
                                if a2 == '1':
                                    continue
                                else:
                                    break
                            elif s_menu == 2:
                                print(student_ob.view_courses_list())
                                a2 = input("1)Continue\n2)Exit")
                                if a2 == '1':
                                    continue
                                else:
                                    break
                            elif s_menu == 3:
                                print(student_ob.select_courses())
                                a2 = input("1)Continue\n2)Exit")
                                if a2 == '1':
                                    continue
                                else:
                                    break
                            elif s_menu == 4:
                                print(student_ob.view_courses_select())
                                a2 = input("1)Continue\n2)Exit")
                                if a2 == '1':
                                    continue
                                else:
                                    break
                            elif s_menu == 5:
                                break
                            else:
                                print('invalid number!')
                                continue
                    n = input('Your username or password is invalid! Do you want try again?(y,n): ')
                    if n == 'y':
                        co += 1
                        continue
                    else:
                        break
                else:
                    print('Your account lock for 5 seconds.')
                    time.sleep(5)
                    log.info_logger.error('User student login failed.')
                    break
                    # else:
                    #     log.warning_logger.error(f"User student doesn't exist.")
                    #     print("Your username or password is invalid! try again.")
                    #     continue
            elif entrance_user == '3':
                cls()
                while True:
                    try:
                        person_type = int(input('Who are you?\n1)Responsible_Training\n2)Student\n3)Exit : '))
                        if person_type == 1:
                            a = register.get_info_r(1)
                        elif person_type == 2:
                            b = register.get_info_r(2)
                            break
                        else:
                            break
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")
            elif entrance_user == '4':
                break
            else:
                print('"Oops!  That was no valid number.  Try again..."')
                continue

        except Exception as v:
            log.warning_logger.error(f'{v}')
            print(v)



print(menu())
