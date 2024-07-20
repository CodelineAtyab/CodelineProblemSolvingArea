import string

username = input("username: ")
password= input('password: ')
email= input('Email: ')

if username!='' and len(username)<=50:
    print("Username is valid ")
else:
    print('Username is invalid')
    
# Special characters using string.punctuation
special_characters = string.punctuation

# Validate Password
password_valid = True

if (len(password) < 8 or
    not any(char in special_characters for char in password) or
    not any(char.isdigit() for char in password) or
    not any(char.isupper() for char in password) or
    not any(char.islower() for char in password)):
        print("Password is invalid")

else:
          print("Password is valid.")

# Split the email into local and domain parts
local_part, domain_part = email.split('@', 1)

 # Check if email contains '@' and a '.' in the domain part
 # Check if the local part before '@' is alphanumeric
 # Check if each part of the domain (split by '.') is alphanumeric
if ("@" not in email or "." not in email.split('@')[-1] or not local_part.isalnum() or not all(part.isalnum() for part in domain_part.split('.'))):
        print("Email is invalid")
else:
# If both local and domain parts are valid, the email is valid
    print("Email is valid.")








 
