#we make rectangle
rows = int(input("how many rows: "))
columns = int(input("how many cols: "))
symbol = input("symbole entre: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()