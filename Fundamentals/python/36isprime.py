def isprime(n):
    n =int(n)
    if n >1:
        for i in range(2,n):
            if(n%i == 0):
                print("this is not prime",n)
                flag =0
                break
                return 0
        else:
                print("this is prime",n)
                return 1
            
n = int(input("the number is: "))
isprime(n)