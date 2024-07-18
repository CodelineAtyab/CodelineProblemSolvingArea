# Solution for Problem 2

def decimal_to_binary(decimal_num):
    
    if decimal_num == 0:
        return "0"

   
    binary_str = ""

   
    while decimal_num > 0:
        remainder = decimal_num % 2    
        binary_str = str(remainder) + binary_str  
        decimal_num //= 2              

    return binary_str



def main():
    
    decimal_num = int(input("Enter a positive decimal number: "))

    
    if decimal_num < 0:
        print("Please enter a positive decimal number.")
        return

    
    binary_result = decimal_to_binary(decimal_num)

    
    print(f"The binary equivalent of {decimal_num} is: {binary_result}")

if __name__ == "__main__":
    main()
