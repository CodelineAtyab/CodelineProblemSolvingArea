#Palindromic traingle starts with 1 , 121  rather than 1, 11, 121 as written in the doc.
def menu():
    print("Menu: ")
    print("1.Display a right-angle triangle of ones.")
    print("2.Display a Palindromic triangle. ")
    print("3.Help.")
    print("4.Exit.")
    choice=input("Enter your choice: ")
    if choice== "1":
        numb=int(input("Enter the number of lines: "))
        for i in range(numb+1):
            print("1"*i)
    elif choice == "2":
        numb2=int(input("Enter the number of lines: "))
        for i in range(1, numb2+1):
            print((111111111//(10**(9-i)))**2)
    #used a mathematical formula

    elif choice == "3":
        print("This program will print lines of one's in the triangular shape of your choice ")
        print("You are presented with two choices, a right angled triangle or a Palindromic triangle. ")
        print("A Palindromic triangle is a triangular array of numbers where each row forms a palindrome. ")
        print("A Palindromic triangle generally follows this pattern: ")
        print("1")
        print("121")
        print("12321")
        print("...")
        print("And so on, depending on the number of lines entered.")
    elif choice== '4':
        print("Exiting the program!")
        quit()



menu()

