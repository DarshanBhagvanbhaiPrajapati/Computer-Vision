input_tuple = (1,2,3,4,5,6)

list = []
#adding reversed values in a list
for x in reversed(input_tuple):
    list.append(x) #we have stored in list and added them

output_tuple = tuple(list) #typecast into tuple
print(output_tuple)
