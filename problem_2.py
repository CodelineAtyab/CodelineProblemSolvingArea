decimal_number = int(input("Input: "))


if decimal_number <= 0:
    print("Please enter a positive number.")
else:
    binary_identical = ""
    
    while decimal_number > 0:
       
        remainder = decimal_number % 2
        # Add the remainder to the front of the binary string
        binary_identical = str(remainder) + binary_identical
        # Update the number to be the quotient of the division
        decimal_number = decimal_number // 2

    print("Output:", binary_identical)
 
