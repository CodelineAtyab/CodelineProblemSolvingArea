import re

def validate_username(username):
    return username != "" and len(username) <= 50

def validate_password(password):
    return len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(char in "!@#$%^&*" for char in password)

def validate_email(email):
    return re.match(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+", email)

username = input("Username: ")
password = input("Password: ")
email = input("Email: ")

if validate_username(username) and validate_password(password) and validate_email(email):
    print("Username is valid.")
    print("Password is valid.")
    print("Email is valid.")
else:
    if not validate_username(username):
        print("Username is invalid.")
        print("Password is valid.")
        print("Email is valid.")
    if not validate_password(password):
        print("Username is valid.")
        print("Password is invalid.")
        print("Email is valid.")
    if not validate_email(email):
        print("Username is valid.")
        print("Password is valid.")
        print("Email is invalid.")