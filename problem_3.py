def display_menu():
    print("Menu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a palindromic triangle")
    print("3. Help")
    print("4. Exit")
    
    
def display_right_angle_triangle():
    n = int(input("Enter the number of lines: "))
    for i in range(1, n + 1):
        print("1 " * i)

def display_palindromic_triangle():
    n = int(input("Enter the number of lines: "))
    for i in range(1, n + 1):
        print(" ".join(str(x) for x in range(1, i + 1)) + " " + " ".join(str(x) for x in range(i - 1, 0, -1)))

def display_help():
    print("help:")
    print("A palindomic triangle is a triangular array of numbers where each row forms a palindrome.")
    
    print("The first few line of a palindromic triangle are: ")
  
    print("1")
    print("1 1")
    print("1 2 1")
    print("1 3 3 1")
    
    print("you can use this pattren to draw a palindromic triangle for any number of line.")
 
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_right_angle_triangle()
        elif choice == '2':
            display_palindromic_triangle()
        elif choice == '3':
            display_help()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
