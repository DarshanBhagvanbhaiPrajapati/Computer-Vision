#lab 6 problem 2
from collections import defaultdict, Counter

test_case = [4, 6, 6, 4, 2,2, 4, 8, 5, 8]

grouped_elements = defaultdict(list)
element_counts = Counter(test_case)

# Iterate through the counts and add elements to the corresponding key in the defaultdict
for element, count in element_counts.items():
    grouped_elements[element].extend([element] * count)

print(grouped_elements)
