def remove_specified_elements(lst):
    modified_list = [elem for index, elem in enumerate(lst) if index not in (0,2, 4,5)]
    return modified_list
specified_list = input("Enter the elements of the list separated by spaces:").split()
specified_list = [int(elem) for elem in specified_list]
result = remove_specified_elements(specified_list)
print("Original List:", specified_list)
print("List after removing specified elements:", result)