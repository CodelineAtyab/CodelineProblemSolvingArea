# Function to generate squares of even numbers
def generate_even_squares(numbers):
    even_squares = [x**2 for x in numbers if x % 2 == 0]
    return even_squares

# Function to slice the list
def slice_list(numbers, start, end):
    return numbers[start:end]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_index = 2
end_index = 7

even_squares = generate_even_squares(numbers)
sliced_list = slice_list(numbers, start_index, end_index)

print("Even squares:", even_squares)
print("Sliced list:", sliced_list)
