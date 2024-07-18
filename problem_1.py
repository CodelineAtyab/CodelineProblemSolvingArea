import re

def validate_username(username):
    if not username:
        return "Username should not be empty."
    if len(username) > 50:
        return "Username should not exceed 50 characters."
    return "Username is valid."

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password should contain at least one special symbol."
    if not re.search(r'[0-9]', password):
        return "Password should contain one or more numbers."
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return "Password should contain both uppercase and lowercase characters."
    return "Password is valid."

def validate_email(email):
    if "@" not in email:
        return "Email should contain '@' symbol."
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Email should be a valid email address."
    return "Email is valid."

def main():
    print("User Login Validation")
    
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")
    
    print("\nValidation Results:")
    print(f"Username: {validate_username(username)}")
    print(f"Password: {validate_password(password)}")
    print(f"Email: {validate_email(email)}")

if __name__ == "__main__":
    main()
