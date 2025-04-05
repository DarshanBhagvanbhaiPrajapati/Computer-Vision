#Write a python program to find the second smallest number in  a list.

num = [2,4,98,123,54,6,1,65]

smallest_num = float('inf')
second_smallest_num = float('inf')

for i in num:
    if i <= smallest_num:
        print("smallest num")
    elif i < second_smallest_num:
        print("second smallest num is ",i)
