#6)wap to count the number of duplicates elemetns in alist

my_list = [1, 2,3,5,6,4,4,2,2,3,6]

duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

if len(duplicates) != 0:
    print("Duplicates:", duplicates)
else:
    print('No duplicates found!')