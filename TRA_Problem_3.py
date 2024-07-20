# TRA Problem 3, Interactive Triangle Display
import time

def menu_option():
    options = ("1", "2", "3", "4")

    while True:
        print("Menu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")

        print()
        choice = input("Enter your choice:")

        if choice in options:
            return choice

        else:
            print("Option invalid")
            time.sleep(1.5)


while True:
    choice = menu_option()
    if choice == "1":
        print()
        user_n = int(input("Enter the number of lines:"))
        for i in range(1, user_n + 1):
            for j in range(1, i + 1):
                print("1", end="")
            print("")
        time.sleep(1.5)
        print()

    elif choice == "2":
        print()
        user_p = int(input("Enter the number of lines:"))
        for i in range(1, user_p + 1):
            print((((10**i)-1)//9)**2)
        time.sleep(1.5)
        print()

    elif choice == "3":
        print()
        print("Help:")
        print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
        print("The first few lines of a Palindromic Triangle are:")
        p = 5
        for i in range(1, p + 1):
            print((((10 ** i) - 1) // 9) ** 2)
        print("You can use this pattern to draw a Palindromic Triangle for any number of lines.")
        time.sleep(1.5)
        print()

    elif choice == "4":
        print()
        print("Exiting the program.")
        exit()