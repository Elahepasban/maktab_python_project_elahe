import log
import hashlib
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
    username = input("Enter your username and password please.\nusername(7character): ")
    password = input('\npassword(7character): ')
    f_id = encode(username, password)
    f = FileHandler(file)
    if f.check_unique_id(f_id):
        return True
    else:
        return False


# def menu():
# text = ..
# text.expandtabs(10)

while True:
    entrance_user = input("Welcome to unit selection system of Science college\nWho are you?\n\n"
                          "1)Responsible_Training\t\t\t\t2)Student\t\t\t\t3)Register\n\nEnter: ")
    try:
        if entrance_user == '1':
            if get_info('responsible_trainings.csv'):
                log.info_logger.info('User responsible training login.')
                print('Welcome to your panel.')
                rt_menu = int(input("1)Create lesson\n2)View student list\n3)View student panel\nNumber: "))
                cls()
                if rt_menu == 1:
                    print(Responsible_Training.create_lesson())
                elif rt_menu == 2:
                    print(Responsible_Training.view_student_list())
                elif rt_menu == 3:
                    print(Responsible_Training.view_student_panel())
                else:
                    print('invalid number!')
                    continue
            else:
                log.warning_logger.error(f"User responsible training doesn't exist.")
                print("Your username or password is invalid! try again.")
                continue
        elif entrance_user == '2':
            os.chdir(r"students")
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
                        print(f'Hi {row["firstname"]} {row["lastname"]}. Welcome to your panel.')
                s_menu = int(input('1)View my information\n2)View courses list\n3)Select courses\n4)'
                                   'view courses selected\nNumber: '))
                student_ob = student.Student(c)
                if s_menu == 1:
                    print(student_ob.view_student_info())
                elif s_menu == 2:
                    print(student_ob.view_courses_list())
                elif s_menu == 3:
                    print(student_ob.select_courses())
                elif s_menu == 4:
                    print(student_ob.view_courses_select())
                else:
                    print('invalid number!')
                    continue
            else:
                log.warning_logger.error(f"User student doesn't exist.")
                print("Your username or password is invalid! try again.")
                continue
        elif entrance_user == '3':
            cls()
            while True:
                try:
                    person_type = int(input('Who are you?\n1)Responsible_Training\n2)Student\n3)Exit'))
                    if person_type == 1:
                        pass
                        # responsible_training_info = get_info(1)

                    elif person_type == 2:
                        pass
                        # student_info = get_info(2)
                    else:
                        break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
        else:
            print('"Oops!  That was no valid number.  Try again..."')
            continue

    except Exception as v:
        log.warning_logger.error(f'{v}')
        print(v)
# print(menu())
