# TRA Problem 1, User Login Validation
import re

Lower = 0
Upper = 0
Special = 0
Number = 0
loweralphabets = "qwertyuiopasdfghjklzxcvbnm"
upperalphabets = "QWERTYUIOPASDFGHJKLZXCVBNM"
specialcharacter = "!@£$%^&*"
number = "1234567890"

pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

while True:
    Username = input("Username: ")
    Password = input("Password: ")
    Email = input("Email: ")

    if len(Username) <= 50:
        print("Username is valid")
    else:
        print("Username is invalid")
    if (len(Password) >= 8):
        for p in Password:
            if (p in loweralphabets):
                Lower += 1
            if (p in upperalphabets):
                Upper += 1
            if (p in number):
                Number += 1
            if (p in specialcharacter):
                Special += 1
            if (Lower >= 1 and Upper >= 1 and Special >= 1 and Number >= 1 and Lower + Upper + Special + Number == len(Password)):
                print("Password is valid")
    else:
        print("Password is invalid")
    if re.match(pattern, Email):
        print("Email is valid")
    else:
        print("Email is invalid")
    break