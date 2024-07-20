#problem 4:Generating Even Squares
def generate_even_squares(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

def slice_sublist(numbers, start_index, end_index):
    return numbers[start_index:end_index]

def main():
    try:
        numbers = list(map(int, input("Enter a list of integers separated by space: ").split()))
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by space.")
        return

    even_squares = generate_even_squares(numbers)
    print(f"List of squares of even numbers: {even_squares}")
    try:
        numbers = list(map(int, input("Enter a list of integers separated by space: ").split()))
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by space.")
        return
    try:
        start_index = int(input("Enter the start index for slicing: "))
        end_index = int(input("Enter the end index for slicing: "))
        if start_index < 0 or end_index > len(numbers) or start_index > end_index:
            print("Invalid indices. Please ensure start index is less than end index and within the bounds of the list.")
            return
    except ValueError:
        print("Invalid indices. Please enter integer values.")
        return

    sublist = slice_sublist(numbers, start_index, end_index)
    print(f"Sliced sublist: {sublist}")

if __name__ == "__main__":
    main()
