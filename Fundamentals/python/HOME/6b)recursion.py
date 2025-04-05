#recursion
#1)counting form n to 1
# def count(n):
#     if n==0: #base case
#         return
#     print(n)
#     count(n-1) #recursive relation
# count(5)
#-----------------------------------------------------------------------
#2)factorial of any number

# n = int(input("entre num == "))

# def factorial(n):
#     if n == 0 or n==1 : #base case
#         return 1
#     else:
#         return  n * factorial(n-1) #recursive relation

# print(factorial(n))
#-----------------------------------------------------------------------
#calculate sum of n naturan numbers

# n = int(input("entre n = "))

# def sum_naturalno(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum_naturalno(n-1)
    
# print(sum_naturalno(n))
#---------------------------------------------------------------------------
#write a recursive function to print all elements in a list(use list and index as parameter)

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

games = ["handball","basketball","bedminton","khokho"]
print_list(games)
        