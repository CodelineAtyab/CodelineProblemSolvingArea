def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    
    return binary

def main():
    try:
        number = int(input("Input: "))
        if number < 0:
            print("Please enter a positive number.")
        else:
            binary = decimal_to_binary(number)
            print(f"Output {binary}")
    except ValueError:
        print("Invalid input! Please enter a positive decimal number.")

if __name__ == "__main__":
    main()
