x = int(input("Enter number: "))
list = []
list2 = []
list3 = []
print("Enter the list of integers: ")  #creating user's list
for i in range(x):
  i = int(input())
  list.append(i)
print(list)
for i in list:  #getting even numbers and the squares of them
  if i % 2 == 0:
    square = i * i
    list2.append(square)
print("List of squares of even numbers: ", list2)
while True:  #getting start and end index
  y = int(input("Start index: "))
  z = int(input("End index: "))
  if 0 <= y < len(list) and y <= z < len(
      list):  #checking index validity & creating sublist
    for i in range(y, z + 1):
      list3.append(list[i])
    print("Sublist:", list3)
    break
  else:
    print("index invalid")
