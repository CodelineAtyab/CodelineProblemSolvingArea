def contains_special_character(s):
    special_characters = "!@#$%^&*()-_+=<>?/"
    for char in s:
        if char in special_characters:
            return True
    return False

def contains_digit(s):
    for char in s:
        if char.isdigit():
            return True
    return False

def contains_uppercase(s):
    for char in s:
        if char.isupper():
            return True
    return False

def contains_lowercase(s):
    for char in s:
        if char.islower():
            return True
    return False

def is_valid_email(email):
    if "@" not in email:
        return False
    local, domain = email.split("@")
    if not local.isalnum():
        return False
    if "." not in domain:
        return False
    domain_name, extension = domain.rsplit(".", 1)
    if not domain_name.isalpha() or not extension.isalpha():
        return False
    return True
def validateUN(username):
    if username == "":
        print("Username is invalid")
        return False
    if len(username) > 50:
        print("Username is invalid")
        return False
    else:
        print("Username is valid")
def validatePW(password):
    if len(password) < 8:
        print("Password is invalid")
        return False
    if not contains_special_character(password):
        print("Password is invalid")
        return False
    if not contains_digit(password):
        print("Password is invalid")
        return False
    if not contains_uppercase(password):
        print("Password is invalid")
        return False
    if not contains_lowercase(password):
        print("Password is invalid")
        return False
    else:
        print("Password is valid")
    
    
def validateEM(Email):
    if not is_valid_email(email):
        print("Email is invalid.")
        return False
    else:
        print("Email is valid.")


username = input("Enter Username: ")
password = input("Enter Password: ")
email = input("Enter Email: ")

print("")
validateUN(username)
validatePW(password)
validateEM(email)

