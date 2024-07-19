def decimal_to_binary(decimal):
    binary = ""

    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2

    return binary


decimal_number = int(input("Enter a positive decimal number: "))
binary_equivalent = decimal_to_binary(decimal_number)

print("The binary equivalent of", decimal_number, "is:", binary_equivalent)
