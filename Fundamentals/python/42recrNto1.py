#printing number from n to till 1

def numbernto1(n):
    if n==0:
        return 
    print(n)
    numbernto1(n-1)

n=int(input())
numbernto1(n)