s = input("Enter a string:=")
f = 0

for i in s:
    if i == 'a' or i == 'A':
        f += 1

print("Total count of frequency of letters 'a'/'A' is",f)
