import ast

list1 = input("Enter the list of integers: ")
print ("part 1 : squares of even numbersin the list")


list = input_list = ast.literal_eval(list1) 


print("List of squares of even numbers : ", [list[i]**2 for i in range(len(list)) if list[i] % 2 == 0])

print ("part 2 : slices the original list to extract the sublist from given start index to the given index")

start = int(input("Enter the start index: "))
end = int(input("Enter the end index : "))


print("sublist: ", [list[x] for x in range(start,end)])