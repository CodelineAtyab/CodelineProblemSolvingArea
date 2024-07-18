# Solution for Problem 3

def display_right_angle_triangle(size):
    for i in range(1, size + 1):
        print("1 " * i)

def display_palindromic_triangle(size):
    for i in range(1, size + 1):
        row = " ".join(str(j % 2) for j in range(1, i + 1))
        print(row)

def display_help():
    print("""
    Help:
    1. Right-Angle Triangle of Ones:
       A right-angle triangle of ones is a triangle where each row contains an increasing number
       of ones. For example, if you choose to display a right-angle triangle with 4 lines, it will 
       look like this:
       1 
       1 1 
       1 1 1 
       1 1 1 1
       
    2. Palindromic Triangle:
       A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.
       A palindrome is a sequence that reads the same backward as forward. Here are the first few 
       lines of a Palindromic Triangle:
       1
       11
       121
       12321
       1234321
       You can use this pattern to draw a Palindromic Triangle for any number of lines.
    """)

def main():
    print("Interactive Triangle Display")

    while True:
        print("""
        Menu:
        1. Display a right-angle triangle of ones
        2. Display a Palindromic Triangle
        3. Help
        4. Exit
        """)

        choice = input("Enter your choice : ")

        if choice == '1':
            size = int(input("Enter the number of lines for the right-angle triangle: "))
            display_right_angle_triangle(size)
        elif choice == '2':
            size = int(input("Enter the number of lines for the palindromic triangle: "))
            display_palindromic_triangle(size)
        elif choice == '3':
            display_help()
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
