from itertools import islice

input_list = input("Enter the list of integers(separated by coma) : ")
original_numbers = [int(number) for number in input_list.replace(' ', '').split(',')]

squared_even = [number**2 for number in original_numbers if number % 2 == 0]
print(f"List of squares of even numbers: {squared_even}")

input_sublist = input("Enter another list of integers(separated by coma)  : ")
numbers_list = [int(number) for number in input_sublist.replace(' ', '').split(',')]

start = int(input("Enter start index: "))
end = int(input("Enter end index: "))


if start < 0 or end > len(numbers_list) or start >= end:
    print("Invalid indices.")
else:
    sublist = list(islice(numbers_list, start, end))
    print(f"Sublist: {sublist}")
 
