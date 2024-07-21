def main():
    input_list = input("Enter a list of integers separated by spaces: ")
    numbers = list(map(int, input_list.split()))

    even_squares = [x**2 for x in numbers if x % 2 == 0]
    print("List of squares of even numbers:", even_squares)

    start_index = int(input("Enter the start index: "))
    end_index = int(input("Enter the end index: "))
    sublist = numbers[start_index:end_index]
    print("Sublist from index", start_index, "to", end_index, ":", sublist)

if __name__ == "__main__": main()
