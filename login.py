import getpass
import dotenv
from dotenv import load_dotenv
import os


load_dotenv()
OLIVIA = os.getenv("OLIVIA")
ETHAN = os.getenv("ETHAN")
BRIANNA = os.getenv("BRIANNA")

# Set program run configuration (see modify options) to emulate terminal in ouput console.
users = {
    'olivia': OLIVIA,
    'ethan': ETHAN,
    'brianna': BRIANNA
}


def denied():
    print('Wrong password! Access Denied.')


def login():
    usr = input('Username: ')
    return usr


def no_user_found():
    print("Please check your records or check with your administrator.")


username_attempts = 2
password_attempts = 3

uname = ''
while True:
    if username_attempts > 0:
        uname = login()
        if uname not in users:
            username_attempts -= 1
            print('User not found!')
        else:
            break
    elif username_attempts == 0:
        no_user_found()
        break

if uname in users:

    while password_attempts > 0:
        password = getpass.getpass('Password: ')
        if password == users[uname]:
            print('Welcome ' + uname.title() + '!')
            break
        else:
            password_attempts -= 1
            denied()
            if password_attempts == 0:
                print("You had too many attempts.")
