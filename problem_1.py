import re

def validate_username(username):
    # Username should not be empty.
    if not username:
        return "Username is invalid"
    # Username should not exceed 50 characters.
    if len(username) > 50:
        return "Username is invalid"
    return "Username is valid."

def validate_password(password):
    # Password must be at least 8 characters long.
    if len(password) < 8:
        return "Password is invalid"
    # Password must contain at least one special symbol.
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password is invalid"
    # Password must contain at least one number.
    if not re.search(r"\d", password):
        return "Password is invalid"
    # Password must contain both uppercase and lowercase characters.
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
        return "Password is invalid"
    return "Password is valid."

def validate_email(email):
    # Email must contain '@' symbol.
    if "@" not in email:
        return "Email is invalid"
    local, _, domain = email.partition("@")
    # Email local part must be alphanumeric.
    if not re.match(r"^[A-Za-z0-9._%+-]+$", local):
        return "Email is invalid"
    # Email domain part must be valid.
    if not re.match(r"^[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", domain):
        return "Email is invalid"
    return "Email is valid."

def main():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")

    print(validate_username(username))
    print(validate_password(password))
    print(validate_email(email))

if __name__ == "__main__":
    main()