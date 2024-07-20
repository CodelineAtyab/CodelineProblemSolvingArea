while True:
    print("Menu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")
    
    decision = int(input("Enter your choice: "))
    
    if decision == 1:
        # Get the number of lines for the right-angle triangle
        lines = int(input("Enter the number of lines: "))
        
        # Print the right-angle triangle of ones
        for i in range(1, lines + 1):
            print('1 ' * i)
    
    elif decision == 2:
        lines = int(input("Enter the number of lines: "))
        
        # Print the palindromic triangle
        for i in range(1, lines + 1):
            # Create the left side of the palindrome
            left_side = ''.join(str(j) for j in range(1, i + 1))
            # reversing the left side except the last character
            right_side = left_side[-2::-1]
            # full palindromic line
            print(left_side + right_side)
    
    elif decision == 3:
        # help message
        print("Help:")
        print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
        print("The first few lines of a Palindromic Triangle are:")
        print("1\n11\n121\n12321\n1234321")
        print("You can use this pattern to draw a Palindromic Triangle for any number of lines.")
    
    elif decision == 4:
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please try again.")
 
