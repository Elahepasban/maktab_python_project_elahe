from student import *
from login import *
import logging
from expect import *
from

def cls():
    print("\n" * 15)

logging.basicConfig(level=logging.DEBUG,filename='app.log', filemode='w',format='%(process)d-%(levelname)s-%(message)s')

print("Welcome to unit selection system of Science college\nWho are you?\n\n"
      "1)Responsible_Training\t\t\t\t2)Student\t\t\t\t3)Register\n")
while True:
    entrance_user = input("Enter: ")
    if entrance_user == '1':
        cls()
    elif entrance_user == '2':
        pass
    elif entrance_user == '3':
        cls()
        while True:
            try:
                person_type = int(input('Who are you?\n1)Responsible_Training\n2)Student\n3)Exit'))
                if person_type == 1:
                    responsible_training_info = get_info(1)

                elif person_type == 2:
                    student_info = get_info(2)
                else:
                    break
                raise ValueError("That is not a right number!")
            except ValueError as ve:
                print(ve)
    else:
        continue
