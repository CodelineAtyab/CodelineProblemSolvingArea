def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"

    binary = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary = str(remainder) + binary
        decimal_num = decimal_num // 2

    return binary


decimal_number = input("Enter a postive decimal: ")
binary_num = decimal_to_binary(int(decimal_number))
print("Output: " + binary_num)
