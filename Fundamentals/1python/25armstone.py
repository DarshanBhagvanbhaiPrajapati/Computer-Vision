
n = int(input("Enter a positive number : "))
sum =0
order = len(str(n))
copy_n= n 

while(n>0):
    digit = n % 10
    sum += digit ** order
    n = n // 10

if (sum == copy_n):
    print("this is armstone number")
else:
    print("this is not armstone number") 

 

