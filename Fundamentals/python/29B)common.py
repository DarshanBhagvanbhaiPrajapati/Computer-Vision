def have_common_member(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return len(set1.intersection(set2)) > 0
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
print("List 1:", list1)
print("List 2:", list2)
print("Do they have at least one common member?",
have_common_member(list1, list2))