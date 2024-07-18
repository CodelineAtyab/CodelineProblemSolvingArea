import re as regex

def validate_username(username):
    if not username:
        return "Username should not be empty."
    elif len(username) > 50:
        return "Username should not exceed 50 characters."
    else:
        return "Username is valid."

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not regex.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password should contain at least one special symbol."
    if not regex.search(r"\d", password):
        return "Password should have one or more numbers."
    if not regex.search(r"[A-Z]", password):
        return "Password should have one or more uppercase characters."
    if not regex.search(r"[a-z]", password):
        return "Password should have one or more lowercase characters."
    return "Password is valid."

def validate_email(email):
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not regex.match(email_regex, email):
        return "Email is not valid."
    return "Email is valid."

def display_menu():
    print("User Login Validation")
    print("=====================")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")

    username_validation = validate_username(username)
    password_validation = validate_password(password)
    email_validation = validate_email(email)

    print(username_validation)
    print(password_validation)
    print(email_validation)

if __name__ == "__main__":
    display_menu()
