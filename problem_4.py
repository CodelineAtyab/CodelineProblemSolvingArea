# Solution for Problem 4

def squares_of_even_numbers(numbers):
    
    even_numbers = [num for num in numbers if num % 2 == 0]
    squares = [num ** 2 for num in even_numbers]
    return squares

def slice_sublist(numbers, start_index, end_index):
   
    sublist = numbers[start_index:end_index + 1]  
    return sublist

def main():
    
    input_numbers = input("Enter the list of integers: ")
    numbers = eval(input_numbers)  

    
    print("Operations:")
    print("1. List of the squares of even numbers")
    print("2. Slice a sublist from the list")

    operation = input("Enter your choice (1 or 2): ")

    if operation == '1':
        
        even_squares = squares_of_even_numbers(numbers)
        print("List of the squares of even numbers:", even_squares)
    elif operation == '2':
        
        start_index = int(input("Enter start index: "))
        end_index = int(input("Enter end index: "))
        if start_index < 0 or end_index >= len(numbers) or start_index > end_index:
            print("Invalid indices. Please enter valid indices.")
        else:
            sublist = slice_sublist(numbers, start_index, end_index)
            print("Sublist:", sublist)
    else:
        print("Invalid choice. Please enter either 1 or 2.")

if __name__ == "__main__":
    main()
