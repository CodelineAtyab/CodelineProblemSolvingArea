import re
def valid_username(x): #username validation function
    return 0 < len(x) <= 50

def valid_password(y): #password validation
    characters = len(y) >= 8 #check character number
    uppercase = re.search(r'[A-Z]', y) #check if uppercase available
    special_characters = re.search(r'[\W_]', y) #check if spesial character available
    number = re.search(r'\d', y) #check if number available
    # Return True only if all conditions are met
    return bool(characters and uppercase and special_characters and number)

def valid_email(email): #emailvalidation
    #check email format
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'
    #using re.match to check if input matches pattern
    return bool(re.match(pattern, email))

def main():
    x = input('Username: ') 
    y = input('Password: ')
    z = input('Email: ')

    if valid_username(x):
        print('Username is valid.')
    else:
        print('Username is invalid.')

    if valid_password(y):
        print('Password is valid.')
    else:
        print('Password is invalid.')

    if valid_email(z):
        print('Email is valid.')
    else:
        print('Email is invalid.')

if __name__ == "__main__":
    main()
