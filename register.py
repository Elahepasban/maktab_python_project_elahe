import hashlib
from file_handler import *
import os


def cls():
    print("\n" * 15)


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


def encoder(u, p):
    b = u + p
    # encode it to bytes using UTF-8 encoding
    message = b.encode()
    i = hashlib.blake2s(message).hexdigest()
    return i


def get_info_r(number):
    if number == 1:
        while True:
            rt_firstname = input('Enter your first name: ')
            rt_lastname = input('Enter your last name: ')
            if rt_firstname.isalpha() and rt_lastname.isalpha():
                print('Next step.')
                cls()
                while True:
                    rt_username = input('Enter your username(7character): ')
                    rt_password = input('Enter your password(7character): ')
                    if len(rt_username) == 7 and rt_password.endswith("004"):
                        print('You register successfully. Remember your username and password.')
                        rt_id = encoder(rt_username, rt_password)
                        rt_info = {'id': rt_id, 'rt_firstname': rt_firstname.strip(),
                                   'rt_lastname': rt_lastname.strip()}
                        rt_file = FileHandler('responsible_trainings.csv')
                        print(rt_file.write_file(rt_info))
                        break
                    else:
                        print("Your username or password is invalid!")
                        continue
                return 'You register successfully.'
            else:
                print('Input should be alphabet! Try again.')
                continue
    elif number == 2:
        while True:
            s_firstname = input('Enter your first name: ')
            s_lastname = input('Enter your last name: ')
            if s_firstname.isalpha() and s_lastname.isalpha():
                s_college = input('Enter your college name(Electricity, Mechanics, Computer, '
                                  'Sciences, Math, Physics, Chemistry): ')
                if check_college(s_college):
                    cls()
                    while True:
                        s_username = input('Enter your username(7character): ')
                        s_password = (input('Enter your password(student number,7character): '))
                        if len(s_username) == 7 and len(s_password) == 7 and s_password.isdigit():
                            s_id = encoder(s_username, s_password)
                            s_info = {'id': s_password, 's_college': s_college, 's_firstname': s_firstname.strip(),
                                      's_lastname': s_lastname.strip()}
                            fields = [s_id, s_password, s_college, s_firstname, s_lastname]
                            s_file = FileHandler('students_list.csv')
                            s_file.write_file(s_info)
                            # create file with header
                            # s_file_name = s_firstname.capitalize().strip() + s_lastname.capitalize().strip() + '.csv'
                            os.chdir(r"students")
                            dirname = s_password.strip()
                            try:
                                # Create target Directory
                                os.mkdir(dirname)
                                os.chdir(dirname)
                                with open(dirname + '.csv', 'w', newline='') as h:
                                    writer = csv.writer(h)
                                    writer.writerow(['id', 'college', 'lesson_name', 'professor_name',
                                                     'unit_number', 'capacity', 'prerequisite', 'score'])
                                with open('information.csv', 'w', newline='') as h:
                                    writer = csv.writer(h)
                                    writer.writerow(['id', 'password', 'college', 'firstname', 'lastname'])
                                    u = csv.writer(h)
                                    u.writerow(fields)
                                print('You register successfully. Remember your username and password.')
                                return 'You register successfully.'
                            except FileExistsError:
                                print("Directory ", dirname, " already exists")
                        else:
                            print("Please enter 7character!")
                            continue
                    break
                else:
                    print('Your college name is invalid! Try again.')
                    continue
            else:
                print('Your name should be alphabet! Try again.')
                continue


# if __name__ == '__main__':
#     print(__name__)

# print('\t' * 14, 'Sequence of username character:\n', '\t' * 10,
#       '1)Number of college  2)Number of Field of Study  3)Entrance year\n', '\t' * 11,
#       'colleges: 1)Electricity 2)Mechanics 3)Computer 4)Sciences\n', '\t' * 6, 'Fields(if your college has'
#     ' not any field of Study enter0): Sciences:{ 0)Math 1)Physics 2)Chemistry }')
# print(get_info_r(2))
