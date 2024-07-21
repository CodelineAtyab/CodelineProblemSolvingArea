def get_even_squares(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

def slice_list(numbers, start, end):
    return numbers[start:end]

def main():
    # Input list of numbers
    numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    
    # Generate squares of even numbers
    even_squares = get_even_squares(numbers)
    print("List of Squares of Even Numbers:", even_squares)
    
    # Slice the original list
    start = int(input("Enter the start index for slicing: "))
    end = int(input("Enter the end index for slicing: "))
    sliced_list = slice_list(numbers, start, end)
    print("Sliced Sublist:", sliced_list)

if __name__ == "__main__":
    main()