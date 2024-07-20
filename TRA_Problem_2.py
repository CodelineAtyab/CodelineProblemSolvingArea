# TRA Problem 4, Generating Even Squares
list = [int(x) for x in input('Please enter a list of numbers: ').split()]

for num in list:
    if num % 2 == 0:
        num2 = num ** 2
        print(num2, end=" ")
print()
list2 = [int(y) for y in input('Please enter a list of numbers: ').split()]
a = int(input("Start index:"))
b = int(input("End index:"))
print(list2[a:b])