
while True:
    print("Menu:\n 1. Display a right angle triangle of ones \n 2. Display a Planidromic triangle \n 3. Help \n 4. Exit")
    input_numb = input("Enter Your choice: ")

    if input_numb == "1":
        number_lines = input("Enter number of lines: ")
        for x in range(int(number_lines)):
            print("1" * (x + 1))
    if input_numb == "2":
        number_lines = input("Enter number of lines: ")
        for i in range(1, int(number_lines) + 1):
            print(int((10 ** i - 1) / 9) ** 2)
    if input_numb == "3":
        print("Help: \n A Palindromic Triangle is triangle array of numbers where each row forms a palindrome. \n The first few lines of a Palindrome Triangle are: \n 1 \n 11 \n 121 \n 12321 \n 1234321 \n You can use this pattern to draw a palindromic Triangle for any number of lines")
    if input_numb == "4":
        break



