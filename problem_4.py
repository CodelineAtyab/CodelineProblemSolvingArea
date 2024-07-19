# Get a list of integers as input
numbers = [int(num) for num in input("Enter the list of integers: ").strip('[]').split(',')]

# Create a new list of squares of even numbers using list comprehension
squares_of_even_numbers = [num**2 for num in numbers if num % 2 == 0]

# Print the list of squares of even numbers
print("List of squares of even numbers:", squares_of_even_numbers)

# Specify the start and end indices for slicing
start_index = int(input("Enter start index: "))
end_index = int(input("Enter end index: "))

# Extract a sublist from the original list based on the start and end indices
sublist = numbers[start_index:end_index+1]

# Print the sliced sublist
print("Sublist:", sublist)
