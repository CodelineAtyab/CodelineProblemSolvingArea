def display_triangle_of_ones(n):
    for i in range(1, n + 1):
        print('1 ' * i)

def display_palindromic_triangle(n):
    for i in range(1, n + 1):
        # Create the increasing part of the line
        increasing_part = ''.join(str(x) for x in range(1, i + 1))
        # Create the decreasing part of the line
        decreasing_part = ''.join(str(x) for x in range(i - 1, 0, -1))
        # Combine both parts and print
        print(increasing_part + decreasing_part)

def display_help():
    print("Help:")
    print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
    print("The first lines of a Palindromic Triangle are:")
    print("1")
    print("11")
    print("121")
    print("12321")
    print("1234321")
    print("You can use this to draw a Palindromic Triangle for any number of lines.")

def main():
    while True:
        print("Menu:")
        print("1. Display right-angle triangle of ones")
        print("2. Display palindromic triangle")
        print("3. Help")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                lines = int(input("Enter the number of lines for the triangle: "))
                if lines <= 0:
                    print("Please enter a positive integer.")
                else:
                    display_triangle_of_ones(lines)
            except ValueError:
                print("Invalid input! Please enter a positive integer.")
        elif choice == '2':
            try:
                lines = int(input("Enter the number of lines for the palindromic triangle: "))
                if lines <= 0:
                    print("Please enter a positive integer.")
                else:
                    display_palindromic_triangle(lines)
            except ValueError:
                print("Invalid input! Please enter a positive integer.")
        elif choice == '3':
            display_help()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()
