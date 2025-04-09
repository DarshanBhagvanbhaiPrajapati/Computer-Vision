file = open("input.txt","r")
# print(file.read())


l1 = file.readlines()
print(l1[1][1])
for i in l1:
    print(i)

# for x in file:
#     print(x)

