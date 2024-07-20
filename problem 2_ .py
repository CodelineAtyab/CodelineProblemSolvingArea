#problem2:covert decimal to binary 
import re
def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    binary_number = ""
    number = decimal_number
    while number > 0:
        remainder = number % 2
        binary_number = str(remainder) + binary_number
        number = number // 2
    return binary_number
# Example usage
decimal_number = int(input("Enter a positive decimal number: "))
binary_number = decimal_to_binary(decimal_number)
print(f"The binary equivalent of {decimal_number} is {binary_number}")
