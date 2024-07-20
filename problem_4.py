def get_squares_of_even_numbers(numbers):
    # Create a new list of squares of even numbers using list comprehension
    squares_of_even_numbers = [x**2 for x in numbers if x % 2 == 0]
    return squares_of_even_numbers

def get_sublist(numbers, start, end):
    # Slice the original list to extract a sublist from start index to end index
    sublist = numbers[start:end]
    return sublist

def main():
    try:
        # Input: List of integers
        numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

        # Perform operations
        squares_of_even_numbers = get_squares_of_even_numbers(numbers)
        print(f"List of squares of even numbers: {squares_of_even_numbers}")

        # Input: Start and end index for sublist
        start_index = int(input("Enter start index: "))
        end_index = int(input("Enter end index : "))

        if start_index < 0 or end_index > len(numbers) or start_index > end_index:
            print("Invalid start or end index.")
        else:
            sublist = get_sublist(numbers, start_index, end_index)
            print(f"Sublist: {sublist}")

    except ValueError:
        print("Invalid input! Please enter integers only.")

if __name__ == "__main__":
    main()
