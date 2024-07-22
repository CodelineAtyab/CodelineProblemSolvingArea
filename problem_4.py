def squares_of_even_numbers(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    squares_of_evens = [num ** 2 for num in even_numbers]
    return squares_of_evens

def slice_sublist(input_list, start_index, end_index):
    sublist = input_list[start_index:end_index + 1]
    return sublist

if __name__ == "__main__":
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_index = 2
    end_index = 4
    
    squares_of_evens = squares_of_even_numbers(original_list)
    print("List of squares of even numbers:", squares_of_evens)
    
    sublist = slice_sublist(original_list, start_index, end_index)
    print(f"Sublist:", sublist)