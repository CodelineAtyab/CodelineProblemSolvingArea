def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    
    binary_num = ''
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2
    
    return binary_num

def main():
    decimal_num = int(input("Enter a positive decimal number: "))
    
    if decimal_num < 0:
        print(" Please enter a positive decimal number.")
    else:
        binary_num = decimal_to_binary(decimal_num)
        print(f" {binary_num}")

if __name__ == "__main__":
    main()




