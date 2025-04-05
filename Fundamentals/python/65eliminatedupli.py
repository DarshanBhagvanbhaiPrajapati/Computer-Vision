#5) wap to eliminate duplicates elements from a list


list = [1,3,4,6,3,3,5,5,6,6,7,3,1]
new_list = list[:]
for i in new_list:
    if list.count(i) > 1:
        list.remove(i)

print(list)