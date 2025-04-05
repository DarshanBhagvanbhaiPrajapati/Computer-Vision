#swapping element index 0 and index 2

# list=[23,65,19,90]
# temp = list[0]   #we have make other variable temp to store first element
# list[0]=list[2]
# list[2]=temp

# print(list)

#using user input

n=int(input("entre the size of list: "))

list=[]
for _ in range(n):
    num=int(input())
    list.append(num)

idx1 = int(input("entre index1: "))
idx2 = int(input("entre index2: "))

print(list)

temp =list[idx1]  #swapping value at idx1 and 2
list[idx2]=list[idx1]
list[idx2]=temp
print(list)
