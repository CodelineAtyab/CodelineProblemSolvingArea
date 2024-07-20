import re

def one_triangle(lines):
    # Function to print an one triangle
    for i in range(1, lines + 1):
        print('1' * i)

def palindromic_triangle(lines):
    # Function to print an palindromic triangle
    for i in range(1, lines + 1):
        # Generate the left side of the palindrome
        left_side = ''.join(str(j) for j in range(1, i + 1))
        # Generate the right side of the palindrome (excluding the middle character)
        right_side = ''.join(str(j) for j in range(i - 1, 0, -1))
        # Print the full palindrome
        print(left_side + right_side)

def help_function():
    # Function to display help information about palindromic triangles
    print("Help:")
    print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
    print("The first few lines of a Palindromic Triangle are:")
    print("1")
    print("11")
    print("121")
    print("12321")
    print("1234321")
    print("You can use this pattern to draw a Palindromic Triangle for any number of lines.")

def triangle_menu():
    # Function to display the menu
    print("1. Display a right-angle Triangle of ones")
    print("2. Display a Palindromics Triangle")
    print("3. Help")
    print("4. Exit")

def main():
    # Main function to run the program
    while True:
        # Display the menu
        triangle_menu()
        # Get user's choice
        choice = int(input("Enter your choice: "))
        if choice == 1:
            # Get the number of lines for the one triangle
            lines = int(input("Enter the number of lines: "))
            one_triangle(lines)
        elif choice == 2:
            # Get the number of lines for the palindrome triangle
            lines = int(input("Enter the number of lines: "))
            palindromic_triangle(lines)
        elif choice == 3:
            # Display help information for palindromic triangle
            help_function()
        elif choice == 4:
            # Exit the program
            print("Exiting the program")
            break
        else:
            # Invalid choice, prompt user to try again
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Run the main function if the script is executed
    main()