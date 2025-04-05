def modifyList(lst):
    lst.append(4)
    print("inside the function: ",lst)

lst =[1,2,3]
modifyList(lst)
print("outside func",lst)