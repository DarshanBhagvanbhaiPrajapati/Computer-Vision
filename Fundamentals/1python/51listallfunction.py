#Write a python program which covers all the methods (functions )of list.

fruits = ["banana","mangoes","oranges","apple"]
fruits.append("kiwi")
print(fruits)

more_fruits = ["guava","papaya"]
fruits.extend(more_fruits)
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.pop(1)
print(fruits)

more_fruits.reverse()
print(more_fruits)

more_fruits.insert(0,["strawberry"])
print(more_fruits)

fruits.sort()
print(fruits)

