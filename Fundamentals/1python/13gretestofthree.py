n1 = int(input("Enter Number 1:="))
n2 = int(input("Enter Number 2:="))
n3 = int(input("Enter Number 3:="))

if n1 > n2 and n1 > n3:
    print("The Number",n1,"is the greatest number.")
if n2 > n1 and n2 > n3:
    print("The Number",n2,"is the greatest number.")
else:
    print("The Number",n3,"is the greatest number.")
