import re

username = input("Enter Username: ")
password = input("Enter Your Password: ")
email = input ("Enter your Email: ")
special_characters = "!@#$%^&*()-+?_=,<>/"
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def has_characters(inputString):
    return any(char in special_characters for char in inputString)

def has_upper(inputString):
    return any(char.isupper() for char in inputString)

def has_lower(inputString):
    return any(char.islower() for char in inputString)


if (len(username) == 0 or len(username) > 50):
    print("Username is Invalid")
else:
    print("Username is Valid")

if (len(password) > 8 and has_characters(password) and has_numbers(password) and has_upper(password) and has_lower(password)):
    print("Password is Valid")
else:
    print("Password is Invalid")

if (re.fullmatch(regex, email)):
    print("Email is Valid")
else:
    print("Email is Invalid")
