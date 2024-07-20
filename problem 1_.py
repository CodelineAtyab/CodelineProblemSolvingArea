#problem1 :User login validation 
import re
def check__validation__input():
  # get name from user
  name = input('Enter Your UserName: ')
  # check if name is mt or length more then 50 cr
  if name == '' or len(name) > 50:
    check__name = 'invalid'
  else:
    check__name = 'valid'
  # get password from user
  password = input('Enter Your Password: ');
  # check length
  if len(password) < 8:
    check__password = 'invalid' 
    # "Password must be at least 8 characters long."
  # check for special symbol 
  elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    check__password = 'invalid' 
    # password should have at last one special symbol.
  # Check for number
  elif not re.search(r"\d", password):
    check__password = 'invalid'
    # "Password must contain at least one number."
  # Check for uppercase and lowercase characters
  elif not re.search(r"[A-Z]", password):
    check__password = 'invalid'
    # "Password must contain at least one uppercase letter."
  # Check for uppercase and lowercase characters
  elif not re.search(r"[a-z]", password):
    check__password = 'invalid' 
    # Password must contain at least one lowercase letter."
  # every thing great
  else:
    check__password = 'valid'
    # everything right ✔
  # check email 
  email = input('Enter Your Email: ')
  at_index = email.find('@')
  check__after = email[at_index+1:]
  dot_index = check__after.find('.')
  before_dot = check__after[:dot_index]
  after_dot = check__after[dot_index + 1:]
  if at_index == -1:
    check__email = 'invalid' 
    # "Email must contain '@' symbol."
  elif dot_index == -1:
    check__email = 'invalid' 
    # domain part must contain '.' symbol
  elif not before_dot.isalpha():
    check__email = 'invalid' 
    # charcters befor '.' in domain must be alphabetic.
  elif not after_dot.isalpha():
    check__email = 'invalid' 
    # charcters after '.' in domain must be alphabetic.
  else:
    check__email = 'valid'
  print('Username is', check__name)
  print('Password is', check__password)
  print('Email is', check__email)

check__validation__input()
