#difference between set is that in set order is not mainained and also indexing not ther
names = {"darshan","ankit","maulik"}
# print(names)

# #length of set
# print(len(names))

# #datatype of set
# print(type(names))

#accesing items of set
# for x in names:
#     print(x)
# #check if item exiists in a set
# if "darshan" in names:
#     print("darsh is there")

# #add elements in set
# names.add("jaimin") #remember same values(duplicates) will not allowed in set
# print(names)

# #add othe sequence
# names_list = ["divy","mihir"]
# names.update(names_list)
# print(names)

# #remove element
# names.remove("mihir")
# print(names)

# names.discard("om") #this function will not throw error if value is not present in set
# print(names)

#join two set
s1={'a','b','c'}
s2={'d','e','a'}

# s3=s1.union(s2)
# print(s3)

# s1.update(s2)
# print(s1)

#keep only duplicates while joining
s1.intersection_update(s2)
print(s1)

#keep all exept duplicated
s1.symmetric_difference_update(s2)
print(s1)