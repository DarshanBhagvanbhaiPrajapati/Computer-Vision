def print_pattern():
    num = 1
    char = 'A'
    for i in range(1, 5):
        if i % 2 != 0:
            for j in range(i):
                print(num, end='')
                num += 1
        else:
            for j in range(i):
                print(char, end='')
                char = chr(ord(char) + 1)
        print()

print_pattern()  