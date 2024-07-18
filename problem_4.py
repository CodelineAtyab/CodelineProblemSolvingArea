def get_even_squares(numbers):
    return [x ** 2 for x in numbers if x % 2 == 0]

def slice_sublist(numbers, start_index, end_index):
    return numbers[start_index:end_index]

def main():
    print("Generating Even Squares and Slicing Sublists")
    print("===========================================")

    # Input the list of integers
    numbers = input("Enter the list of integers (comma separated): ")
    numbers = [int(x.strip()) for x in numbers.split(',')]
    
    # Generate list of squares of even numbers
    even_squares = get_even_squares(numbers)
    print(f"List of squares of even numbers: {even_squares}")

    # Input start and end indices for slicing
    start_index = int(input("Enter start index for sublist: "))
    end_index = int(input("Enter end index for sublist: "))
    
    # Slice the sublist
    sublist = slice_sublist(numbers, start_index, end_index)
    print(f"Sublist: {sublist}")

if __name__ == "__main__":
    main()
