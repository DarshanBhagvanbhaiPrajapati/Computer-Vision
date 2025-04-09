def remove_elements(lst, elements):
  return list(filter(lambda x: x not in elements, lst))
original_list = [1, 2, 3, 4, 5]
elements_to_remove = [2, 4]
new_list = remove_elements(original_list,
elements_to_remove)
print("New List:", new_list)
