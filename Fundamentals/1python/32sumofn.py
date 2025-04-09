#using function
#sum of n
def sumOneToN(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

n=int(input("entre n: "))

#call function
output = sumOneToN(n)
print("sum of all numbers till n is",output)  #always call function after define it
