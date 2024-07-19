def display_menu():
    print("Menu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")

def display_right_angle_triangle(rows):
    for i in range(1, rows + 1):
        print("1 " * i)

def display_palindromic_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + " ".join(str(j) for j in range(i, 0, -1)) + " ".join(str(j) for j in range(2, i + 1)) + " " * (rows - i))

def help_message():
    print("This program displays different patterns of triangles.")
    print("Option 1: Display a right-angle triangle of ones.")
    print("Option 2: Display a Palindromic Triangle.")
    print("Option 3: Help - Display this menu.")
    print("Option 4: Exit - Terminate the program.")

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        rows = int(input("Enter the number of rows for the right-angle triangle: "))
        display_right_angle_triangle(rows)
    elif choice == '2':
        rows = int(input("Enter the number of rows for the palindromic triangle: "))
        display_palindromic_triangle(rows)
    elif choice == '3':
        help_message()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")

