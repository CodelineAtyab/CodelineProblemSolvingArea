print("Menu:")
print("1. Display a right-angle triangle of ones")
print("2. Display a Palindromic Triangle")
print("3. Help")
print("4. Exit")

choise = input("Enter your choice: ")


if choise == "1" :
    lines = int(input("Enter your number of lines: "))
    for line in range(lines+1):
       print(("1 ") * line)
       print("")
elif choise == "2" : 
    lines = int(input("Enter your number of lines: "))
   
    for i in range(1,lines + 1):
     print(int("1" * i)**2)
elif choise == "3" : 
    info = """
          Palindromic Triangle is a triangular array of numbers where each row forms a palindrome. The first few lines of a Palindromic Triangle are:
          1
          11
          121
          12321
          1234321
          You can use this pattern to draw a Palindromic Triangle for any number of lines.
         """
    print(info)

else : 
    print("Exiting the program")
