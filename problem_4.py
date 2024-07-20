def get_even_squares(nums):
    return [x**2 for x in nums if x % 2 == 0]

def slice_list(nums, start, end):
    return nums[start:end+1]

def main():
    # Example list of integers
    nums = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    
    # Generating the list of squares of even numbers
    even_squares = get_even_squares(nums)
    print("List of squares of even numbers:", even_squares)
    
    # Getting start and end indices for slicing
    start = int(input("Enter the start index for slicing: "))
    end = int(input("Enter the end index for slicing: "))
    
    # Slicing the list
    sliced_list = slice_list(nums, start, end)
    print("Sliced list:", sliced_list)

if __name__ == "__main__":
    main()
