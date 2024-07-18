# Solution for Problem 1

import re

def validate_username(username):
    
    if len(username) == 0:
        return "invalid", "Username cannot be empty."
    if len(username) > 50:
        return "invalid", "Username cannot exceed 50 characters."
    return "valid", "Username is valid."

def validate_password(password):
    
    if len(password) < 8:
        return "invalid", "Password must be at least 8 characters long."
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "invalid", "Password must contain at least one special symbol."
    if not re.search("[0-9]", password):
        return "invalid", "Password must contain at least one digit (0-9)."
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return "invalid", "Password must contain both uppercase and lowercase letters."
    return "valid", "Password is valid."

def validate_email(email):
    
    if "@" not in email:
        return "invalid", "Email must contain '@' symbol."
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "invalid", "Invalid email format."
    return "valid", "Email is valid."

def main():
    print("User Login Validation Program\n")
    
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()
    email = input("Enter Email: ").strip()

    username_valid, username_message = validate_username(username)
    password_valid, password_message = validate_password(password)
    email_valid, email_message = validate_email(email)

    print("\nOutput:")
    print("Username:", username_message if username_valid == "valid" else f"Invalid {username_message}")
    print("Password:", password_message if password_valid == "valid" else f"Invalid {password_message}")
    print("Email:", email_message if email_valid == "valid" else f"Invalid {email_message}")

if __name__ == "__main__":
    main()

