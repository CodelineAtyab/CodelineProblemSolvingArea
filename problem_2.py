import re

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def main():
    number = int(input("Input: "))
    if number < 0:
        print("Please enter a positive number.")
    else:
        print(f"Output: {decimal_to_binary(number)}")

if __name__ == "__main__":
    main()