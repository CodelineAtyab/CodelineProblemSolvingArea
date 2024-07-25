def display_right_angle_triangle(size):
    for i in range(1, size + 1):
        print('1 ' * i)

def display_palindromic_triangle(size):
    for i in range(1, size + 1):
        # Generate the left side of the triangle
        left_side = ''.join(str(x) for x in range(1, i + 1))
        # Generate the right side of the triangle by reversing the left side, except the last character
        right_side = left_side[:-1][::-1]
        # Combine both sides to form the full row
        print(left_side + right_side)

def show_help():
    print("Help:")
    print("1. Display a right-angle triangle of ones - This option will display a right-angle triangle with ones.")
    print("2. Display a Palindromic Triangle - This option will display a palindromic triangle.")
    print("3. Help - This option displays this help message.")
    print("4. Exit - This option exits the program.")

def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            size = int(input("Enter the size of the triangle: "))
            display_right_angle_triangle(size)
        elif choice == '2':
            size = int(input("Enter the size of the triangle: "))
            display_palindromic_triangle(size)
        elif choice == '3':
            show_help()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
