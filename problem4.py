list_int = input("Enter List of integers: ")
start_index = int(input("Enter start index: "))
end_index = int(input("Enter End Index: "))

array_char = list_int.replace(' ','').replace('[','').replace(']','').split(',')
array_int = list(map(int,array_char))
print("Square Number List: ", end="[")
for num in array_int:
    if num % 2 == 0:
        print(num ** 2, end=", ")

print("]\nSublist: ", end ="")
print( array_int[start_index:end_index])