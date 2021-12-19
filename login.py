def get_info(number):
    while True:
        if number == 1:
            responsible_training_firstname = input('Enter your first name: ')
            responsible_training_lastname = input('Enter your last name: ')
            if responsible_training_firstname.isalpha() and responsible_training_lastname.isalpha():
                responsible_training_username = responsible_training_firstname+' '+responsible_training_password
                print(f'Your username is: {responsible_training_username} ')
            responsible_training_password = input('Enter your password: ')
            if responsible_training_password:
                {"id": 1, "name": "fateme", "last_name": "soleimani"}
                return [responsible_training_username, responsible_training_password]
            else:
                print('Username or Password is invalid!')
                continue
        elif number == 2:
            student_firstname = input('Enter your first name: ')
            student_lastname = input('Enter your last name: ')
            print('\t' * 14, 'Sequence of username character:\n', '\t' * 10,
                  '1)Number of college  2)Number of Field of Study  3)Entrance year\n', '\t' * 11,
                  'colleges: 1)Electricity 2)Mechanics 3)Computer 4)Sciences\n', '\t' * 6, 'Fields(if your college has'
                  ' not any field of Study enter0): Sciences:{ 0)Math 1)Physics 2)chemistry }')
            student_username = input('Enter your username: ')
            student_password = input('Enter your password: ')
            if student_username.isdigit() and student_password:
                return [student_username, student_password]
            else:
                print('Username or Password is invalid!')
                continue
