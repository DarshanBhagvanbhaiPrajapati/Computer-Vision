#3)wap to count the number of even and odd elements in a list

list = [2,4,6,7,9,23,44]

even = 0
for i in range(0,len(list)):
    if i %2 == 0:
        even += 1
       
print("even number in list is",even)
print("odd number is",len(list)-even)
