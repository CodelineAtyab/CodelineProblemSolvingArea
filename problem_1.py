import re

def validate_username(username):
    if len(username) == 0:
        return False, "is in valid."
    elif len(username) > 50:
        return False, "is in valid."
    else:
        return True, "is valid."

def validate_password(password):
    if len(password) < 8:
        return False, "is in valid."
    elif not re.search("[!@#$%^&*()_+{}[\]:;<>,.?/~\\-]", password):
        return False, "is in valid."
    elif not re.search("[0-9]", password):
        return False, "is in valid."
    elif not re.search("[A-Z]", password):
        return False, "is in valid."
    elif not re.search("[a-z]", password):
        return False, "is in valid."
    else:
        return True, "is valid."

def validate_email(email):
    if "@" not in email:
        return False, "is in valid."
    
    username, domain = email.rsplit('@', 1)
    
    if not username.replace('.', '').isalnum():
        return False, "is in valid."
    
    if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        return False, "is in valid."
    
    return True, "is valid."

def main():
    print("Welcome! enter your details:")
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    

    is_valid_username, username_message = validate_username(username)
    if not is_valid_username:
        print(username_message)
        return
    

    is_valid_password, password_message = validate_password(password)
    if not is_valid_password:
        print(password_message)
        return
    

    is_valid_email, email_message = validate_email(email)
    if not is_valid_email:
        print(email_message)
        return
    
    print("Username is valid")
    print("Password is valid")
    print("Email is valid")

if __name__ == "__main__":
    main()


