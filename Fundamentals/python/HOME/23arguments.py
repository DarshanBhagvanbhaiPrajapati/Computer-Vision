# *args = parameters that will pack all argumetns into a tuple
#         useful so that a function can accept a varying amount of arguments


def add(*args): #we can write other name also in place of *args
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,5))