import hashlib
from getpass import getpass
import getpass

user_password_dict = {}
log_ins = {}
non_log_ins = {}

def hash_password(plain_password):
    return hashlib.sha224(plain_password.encode("UTF-8")).hexdigest()


def new_user():
    username = input("Enter username\n")
    password = input("Enter password\n")
    password = input("Enter password again\n")
    hashedPassword = hash_password(password)
    user_password_dict[username] = hashedPassword
    log_ins[username] = 1
    non_log_ins[username] = 0
    return username

def update_password():
    username = input("\nEnter username: ")
    password = getpass.getpass("\nEnter password: ")
    hashedPassword = hash_password(password)
    if hashedPassword == user_password_dict.get(username):
        print("\nEnter new password: ")
        password = getpass.getpass("\nEnter password: ")
        hashedPassword = hash_password(password)
        user_password_dict[username] = hashedPassword
        print("\nPassword updated")
    else:
        print("Wrong credentials\n")

def login():
    username = input("\nUsername: ")
    logins = log_ins.get(username)
    password = getpass.getpass('Password: ')
    hashedPassword = hash_password(password)

    if hashedPassword == user_password_dict.get(username):
        logins += 1
        log_ins[username] = logins
        print("\nUser " + username + " is now logged in.\nSuccessful logins " + str(logins))
    else:
        if username in log_ins:
            non_log_ins[username] += 1
            print("\nWrong password\n")
        else:
            print("\nNon-registered user or wrong password\n")


def display_users():
    print("\nusernames\tpasswords\t\t\t\t\t\t\t\t\t\t\t\t\tsuccessful logins\t\t\tunsuccessful logins\n")
    length = len(log_ins)
    usernames = log_ins.keys()
    for key in log_ins:
        print(key + "\t\t\t" + user_password_dict[key] + "\t" + str(log_ins[key]) + "\t\t\t\t\t\t\t" + str(non_log_ins[key]) + "\n")

if __name__ == "__main__":
    while True:
        print("1. Sign up 2. Update password 3. Login 4. List users")
        choice = input("Enter your choice: ")
        if choice == "":
            break
        elif choice == "1":
            username = new_user()
            print("\nThe user " + username + " was added to the system")
        elif choice == "2":
            update_password()
        elif choice == "3":
            login()
        elif choice == "4":
            display_users()