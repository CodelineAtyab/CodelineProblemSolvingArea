def right_angle_triangle(lines):
    for i in range(1, lines + 1):
        print('1 ' * i)

def palindromic_triangle(lines):
    for i in range(1, lines + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        for j in range(i - 1, 0, -1):
            print(j, end=' ')
        print()

def display_help():
    print("\nHelp:")
    print("1. Right-angle Triangle of Ones:")
    print("   This option displays a right-angled triangle made of '1's.")
    print("   The number of lines determines the height of the triangle.")
    print("\n2. Palindromic Triangle:")
    print("   This option displays a triangle with palindromic number patterns.")
    print("   Each line is a palindrome, and the number of lines determines")
    print("   the size of the triangle.")

def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a palindromic triangle")
        print("3. Help")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            lines = int(input("Enter the number of lines: "))
            right_angle_triangle(lines)
        elif choice == '2':
            lines = int(input("Enter the number of lines: "))
            palindromic_triangle(lines)
        elif choice == '3':
            display_help()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()