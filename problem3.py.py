def display_menu():
    print("Menu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a palindromic triangle")
    print("3. Help")
    print("4. Exit")
    
def right_angle_triangle(n):
     for i in range(1, n + 1):
         print("1 " * i)

def palindromic_triangle(n):
    for i in range(1, n + 1):
    
      for j in range(1, i + 1):
         print(j, end=" ")
      for j in range(i - 1, 0, -1):
          print(j, end=" ")
      print()

def help_message():
    print("Help:")
    print("1. Choose option 1 to display a right-angle triangle of ones.")
    print("2. Choose option 2 to display a palindromic triangle.")
    print("3. Choose option 3 to display this help message.")
    print("4. Choose option 4 to exit the program.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter the number of rows for the triangle: "))
            right_angle_triangle(n)
        elif choice == "2":
            n = int(input("Enter the number of rows for the triangle: "))
            palindromic_triangle(n)
        elif choice == "3":
            help_message()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
            
if __name__ == "__main__": main()
