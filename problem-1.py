import re

def validate_username(username):
    if not username:
        return False, "Username cannot be empty."
    if len(username) > 50:
        return False, "Username cannot exceed 50 characters."
    return True, "Username is valid."

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special symbol."
    if not re.search(r'\d', password):
        return False, "Password must contain at least one number."
    if not (re.search(r'[A-Z]', password) and re.search(r'[a-z]', password)):
        return False, "Password must contain both uppercase and lowercase characters."
    return True, "Password is valid."

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$'
    if not re.match(email_regex, email):
        return False, "Invalid email format."
    return True, "Email is valid."

def main():
    print("User Login Validation")
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")

    username_valid, username_msg = validate_username(username)
    password_valid, password_msg = validate_password(password)
    email_valid, email_msg = validate_email(email)

    print("\nValidation Results:")
    print(f"Username: {username_msg}")
    print(f"Password: {password_msg}")
    print(f"Email: {email_msg}")

    if username_valid and password_valid and email_valid:
        print("\nAll inputs are valid. Login successful!")
    else:
        print("\nLogin failed. Please correct the errors and try again.")

if __name__ == "__main__":
    main()