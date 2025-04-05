#set = collection which is unorderd , unindexed , no duplicates values
#they do not allow any duplicates value
#it is faster if we need to access any elements

utensil = {"fork","spoon","knife","knife","knife"}
dishes = {"bowl","plate","cup","knife"}

# utensil.add("napkin")
# utensil.remove("fork")
# utensil.clear()
# utensil.update(dishes) #all elements of dishes into utensil

# dinner_table = utensil.union(dishes)


# for x in dinner_table:
#     print(x)

print(utensil.difference(dishes)) #utensil elements that not in dishes


