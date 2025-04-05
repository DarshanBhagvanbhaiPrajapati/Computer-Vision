#creating a tuple
colours = ("red","yellow","white")

#creating a tuple with 1 item
fruit = ("apple",) #we need to add comma after writing one element in tuple
 #otherwise we dont store it or writelike
fruit = tuple(("apple"))

#check type of tuple
print(type(fruit))

#checking length
print(len(colours))

#accesing items in tuple
print(colours[0])  #positive indexing
print(colours[-1]) #negative indexing
print(colours[1:3]) #range indexing printing element at index 1 and 2
print(colours[-2:]) #-ve rane indexing

#check if an item exist in touple
if "white" in colours:
    print("green is ther")
else:
    print("it is not here") 

#traverse the tuple
for i in colours:
    print(i)

#concatenate 2 tuples
more_colors = ("blue","brown")
colours = colours + more_colors
print(colours)

#unpacking a tuple
colour1, colour2, colour3 = colours
print(colour1, colour2, colour3)