import re

def validate_username(username):
    if not username:
        return False, "Username is invalid."
    if len(username) > 50:
        return False, "Username is invalid."
    return True, "Username is valid."

def validate_password(password):
    if len(password) < 8:
        return False, "Password is invalid."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password is invalid."
    if not re.search(r'\d', password):
        return False, "Password is invalid."
    if not re.search(r'[A-Z]', password):
        return False, "Password is invalid."
    if not re.search(r'[a-z]', password):
        return False, "Password is invalid."
    return True, "Password is valid."

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, email):
        return False, "Email is invalid."
    return True, "Email is valid."

def main():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")

    username_valid, username_message = validate_username(username)
    print(username_message)

    password_valid, password_message = validate_password(password)
    print(password_message)

    email_valid, email_message = validate_email(email)
    print(email_message)



if __name__ == "__main__":
    main()
