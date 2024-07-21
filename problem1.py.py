import re
def validate_username(username):
    if not username:
        return "Username should not be empty."
    if len(username) > 50:
        return "Username should not exceed more than 50 characters."
    return None

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password should contain at least one special symbol."
    if not re.search(r'\d', password):
        return "Password should contain one or more numbers."
    if not re.search(r'[A-Z]', password):
        return "Password should contain one or more numbers."
    if not re.search(r'[A-Z]', password):
        return "Password should contain one or more uppercase characters."
    if not re.search(r'[a-z]', password):
        return "Password should contain one or more lowercase characters."
    return None

def validate_email(email):
    if '@' not in email:
        return "Email should contain '@' symbol."
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return "Invalid email format."
        return None
    
def main():
    while True:
        print("Menu:")
        print("1. Enter Username")
        print("2. Enter Password")
        print("3. Enter Email")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            username = input("Enter Username: ")
            username_error = validate_username(username)
            if username_error:
                print("Error:", username_error)
            else:
                print("Username is valid.")
                
        elif choice == "2":
            password = input("Enter Password: ")
            password_error = validate_password(password)
            if password_error:
                print("Error:", password_error)
            else: print("Password is valid.")

        elif choice == "3":
            email = input("Enter Email: ")
            email_error = validate_email(email)
            if email_error: print("Error:", email_error)
            else: print("Email is valid.")
            
        elif choice == "4":
            print("Exiting the program.")
            break
        
        else: print("Invalid choice, please try again.")
        
if __name__ == "__main__": main()
                
