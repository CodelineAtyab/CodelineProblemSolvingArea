import re
#menu, ask for details, then validate.
#create funcs to obtain input.
def displayofmenu():
    print("Welcome to the program, please enter your details below: ")

def obtainuser():
    usern=input("Username: ").strip()
    return usern

def obtainpwd():
    pwd=input("Password: ")
    return pwd

def obtainemail():
    email=input("Email: ")
    return email

#create diff funcs to validate
def emailvalid(email):
    if not re.match(r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.[a-zA-Z]+(?:\.[a-zA-Z]+)*$", email):
        return "Email is invalid."
    else:
        return "Email is valid."

def pwdvalid(pwd):
    if (len(pwd) < 8 or
            #find digit in pwd
            not re.search(r'\d', pwd) or
            #find at least one capital letter
            not re.search(r'[A-Z]', pwd) or
            #find at least one small letter
            not re.search(r'[a-z]', pwd) or
            #find a special character
            not re.search(r'[!#@%$*+£^=&()_-]', pwd)):
        return "Password is invalid."
    else:
        return "Password is valid."

def uservalid(usern):
    if len(usern) == 0 or len(usern) > 50:
        return "Username is invalid."
    else:
        return "Username is valid."


displayofmenu()
usern=obtainuser()
pwd=obtainpwd()
email=obtainemail()
uservalid(usern)
print(uservalid(usern))
pwdvalid(pwd)
print(pwdvalid(pwd))
emailvalid(email)
print(emailvalid(email))