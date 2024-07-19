#import regix for matching
import re

def val_username(username) : 
    #validate that not empty and it length
    if not username or len(username) > 50 : 
        return "invalid"
    else : 
        return "valid"
        

def val_password(password) :  
    #using regix , first part validate all special case , then validate at least one smaller case ... etc 
    if re.match(r'^(?=.*[!@#$%^&*(),.?":{}|<>])(?=.*\d)(?=.*[A-Z])(?=.*[a-z]).{8,}$', password):
        return "valid"
    else:
        return "invalid"
    

def val_email(email) :
    #chick if there is @ , then if yes chick the remaining 
    if "@" in email: 
        before, after = email.split("@", 1)
        if not before.isalnum() or not re.match(r"[a-zA-Z0-9]+\.[a-zA-Z]{2,}$", after):
            return "invalid"
        else : 
            return "valid"
    else : 
        return "invalid"
    
#input process
username = input("Username: ")
password = input("Password: ")
email = input("Email: ") 


#output process
print("Username is ", val_username(username))
print("Password is ", val_password(password))
print("Email is ", val_email(email))

