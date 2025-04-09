#lab 6 problem 6

def func(x):
    index =1#will sort first index if we have to index 2 we will write 2
    return x[index]

t1= (('a',23,5),('b',37,7),('c',11,12),('d',29,3))
print(tuple(sorted(t1,key=func)))

