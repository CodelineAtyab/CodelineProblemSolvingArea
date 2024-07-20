import re

def generate_even_squares(nums):
    #Generate a list of squares of even numbers from the input list.
    return [x ** 2 for x in nums if x % 2 == 0 and x % 2 == 0]

def slice_sublist(nums, start, end):
    #Return a sublist from the input list.
    return nums[start:end]

def main():
    # Get user input for the list of integers
    nums = list(map(int, input("Enter a list of integers (comma-separated): ").split(',')))

    # Get user input for the start and end indices
    start = int(input("Enter start index: "))
    end = int(input("Enter end index: "))
    # Generate and print the list of squares of even numbers
    even_squares = generate_even_squares(nums)
    print("List of squares of even numbers:", even_squares)

    # Slice and print the sublist
    sliced_list = slice_sublist(nums, start, end)
    print("Sublist:", sliced_list)

if __name__ == "__main__":
    main()
