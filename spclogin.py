import getpass
import dotenv
from dotenv import load_dotenv
import os
import sys


# Set program run configuration (see modify options) to emulate terminal in ouput console.

load_dotenv()
admin_password = os.getenv("SPC_KEY")


class User:
    def __init__(self, idnum, first_name, last_name, email, pmt_method='VISA'):
        self.idnum = idnum
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pmt_method = pmt_method

    def describe_user(self):
        user = [self.idnum, self.first_name, self.last_name, self.email, self.pmt_method]
        print(f"A user has been locked out of the system and has emailed requesting an unlock.\nHere is the client summary for User No."
              f" {self.idnum}:")
        for u in user[1:]:
            print(f"\t{u}")
        return ''

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}. Welcome to the \033[35mTeam!\033[39m")


class Admin:
    """Gives an Administrator access to special functions. Note: color codes are not compatible with the getpass module."""
    def __init__(self, idnum, first_name, last_name):
        self.idnum = idnum
        self.first_name = first_name
        self.last_name = last_name

    sh = User(4501, 'Samantha', 'Haggerty', 'shag@gmail.com')

    def unlock(self):
        """Unlocks and resets a specified user id."""
        counter = 1
        while True:
            userid = input("Enter the user id that needs to be unlocked: ")
            print(Admin.sh.first_name, Admin.sh.last_name)
            correct = input("Is this correct? (y/n): ")
            if correct.lower() == 'y':
                break
            else:
                continue
        while True:
            spcid = getpass.getpass("Please enter your special id number: ")
            if spcid == admin_password:
                print(f"User {userid} has been unlocked and reset by Admin - {self.first_name} {self.last_name}.")
                break
            if spcid != admin_password:
                print("That id number does not have Admin authorization.")
                counter += 1
            if counter < 3:
                continue
            else:
                print("You are not authorized.")
                break


def loginAdmin():
    """Logs in an Admin and creates an instance of the Admin  Class."""
    admins = [('80', 'David', 'Jem'), ('90', 'Suzie', 'Jing'), ('100', 'George', 'Franks')]
    Go = True
    while Go:
        try:
            a, b, c = input("Please log in with <id, first name, last name>: \n\t").split(", ")
            if (a, b, c) not in admins:
                print("That is not an authorized admin name or id.")
                sys.exit()
            else:
                admin = Admin(int(a), str(b), str(c))
                print(f"Welcome Administrator {b[0]}{c[0]}!")
                break
        except ValueError:
            print("Please enter each value, separated by a comma and one space.")
            continue
    return admin


def admin_func():
    """Asks the Admin which function to execute.  If a valid function of the Admin class is entered, it is automatically executed.  Enter function based on the instance (admin) as: <admin unlock>.
        The program automatically replaces the space with a dot and adds the parenthesis to the end and executes the function."""
    if admin:
        selection = input("Enter the function you wish to execute preceded by the word 'admin' and one space: ")
    return selection


print(Admin.sh.describe_user())
admin = loginAdmin()
func = str(admin_func()).replace(" ", ".")
function = str(func + "()")
eval(function)
