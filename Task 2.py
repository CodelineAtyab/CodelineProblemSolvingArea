x=int(input("Input: "))
binary_format = []
while x > 0:
  remainder = x % 2  # Recording the remainder
  binary_format.append(str(remainder))  # Appending remainder as a string to list
  x = x // 2  # Updating quotient
binary_format.reverse()
binary_string = ''.join(binary_format)
print(f"Output: {binary_string}") 