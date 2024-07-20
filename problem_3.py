def display_right_angle_triangle(n):
    for i in range(1, n + 1):
        print('1 ' * i)

def display_palindromic_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        for j in range(i - 1, 0, -1):
            print(j, end='')
        print()

def display_help():
    print("Help:")
    print("1. Display a right-angle triangle of ones - This option will display a right-angle triangle of '1's with the number of rows specified by the user.")
    print("2. Display a Palindromic Triangle - This option will display a palindromic triangle with the number of rows specified by the user.")
    print("3. Help - This option displays information about the available menu options.")
    print("4. Exit - This option exits the program.")

def display_menu():
    print("Menu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter the number of rows: "))
            display_right_angle_triangle(n)
        elif choice == "2":
            n = int(input("Enter the number of rows: "))
            display_palindromic_triangle(n)
        elif choice == "3":
            display_help()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
