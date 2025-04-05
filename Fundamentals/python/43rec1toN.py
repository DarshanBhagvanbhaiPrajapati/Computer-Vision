#sum of 1 to n
def sum1ton(n):
    if n==1:
        return 1
    
    ans = n + sum1ton(n-1)
    return ans

n = int(input())
print(sum1ton(n))