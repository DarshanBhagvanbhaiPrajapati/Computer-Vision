def print_pattern(num_lines):
  for i in range(1, num_lines + 1):
    if i % 4 == 1:
     print("1")
    elif i % 4 == 2:
     print("AB")
    elif i % 4 == 3:
     print("234")
    else:
     print("ABCD")
num_lines = int(input("Enter the number of lines: "))
print_pattern(num_lines)