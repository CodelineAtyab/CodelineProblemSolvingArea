#problem 3:interactive triangle display 
import re 
def display_right_angle_triangle(lines):
    for i in range(1, lines + 1):
        print('1' * i)

def display_pallindromic_triangle(lines):
    for i in range(1, lines + 1):
        print(str(1) + ''.join(str(x) for x in range(2, i+1)) + ''.join(str(x) for x in range(i-1, 0, -1)))

def display_help():
    help_text = """
    Help:
    A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.
    The first few lines of a Palindromic Triangle are:
    1
    121
    12321
    1234321
    123454321
    You can use this pattern to draw a Palindromic Triangle for any number of lines.
    """
    print(help_text)

def main():
    while True:
        print("Menu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            lines = int(input("Enter the number of lines: "))
            display_right_angle_triangle(lines)
        elif choice == 2:
            lines = int(input("Enter the number of lines: "))
            display_pallindromic_triangle(lines)
        elif choice == 3:
            display_help()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
