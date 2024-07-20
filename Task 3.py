def right_angle(lines): #creating right angle triangle
  for i in range(1, lines + 1):
      print(" ".join(["1"] * i))
def palindromic(lines): #creating palindromic triangle
  for i in range(1, lines + 1):
      left = " ".join(str(j) for j in range(1, i + 1))
      right = " ".join(str(k) for k in range(i - 1, 0, -1))
      print(left + " " + right)

def help(): 
  print("Help\nA palindromic triangle is a triangular array of numbers where each row forms a palindrome. \nThe first few rows in a palindromic triangle are: \n1 \n1 2 1 \n1 2 3 2 1\n1 2 3 4 3 2 1\n1 2 3 4 5 4 3 2 1\nYou can use this pattern to draw a palindromic triangle for any number of lines.")

def main():
  while True:
      try:
          number = int(input("Menu:\n"
                             "1. Display a right-angle triangle of ones\n"
                             "2. Display a palindromic triangle\n"
                             "3. Help \n"
                             "4. Exit\n"
                             "Enter your choice: "))
          if number == 1:
              lines = int(input("Enter the number of lines: "))
              right_angle(lines)
          elif number == 2:
              lines = int(input("Enter the number of lines: "))
              palindromic(lines)
          elif number == 3:
              help()
          elif number == 4:
              print("Exiting the program")
              break
          else:
              print("Error: Please enter a number from the menu.")
      except ValueError:
          print("Error: Invalid input. Please enter a valid number.")

if __name__ == "__main__":
  main()
