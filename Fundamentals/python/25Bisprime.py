def isPrime(n):
    c = 0
    for i in range(1,n+1):
        if n % i == 0:
            c += 1

    if c == 2:
        return 1
    else:
        return 0

n = int(input("Enter any Number:="))
p = isPrime(n)

if p == 1:
    print("The given Number",n,"is Prime Number")
else:
    print("The given Number",n,"is Not a Prime Number")
