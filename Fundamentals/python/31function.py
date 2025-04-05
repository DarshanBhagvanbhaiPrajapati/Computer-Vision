#print hello

# def printHello():
#     #body of function
#     print("hello world;;")

# printHello()  #calling a function


#function which takes 2 number as input and returns their sum
def add(n1,n2):  #hear n1 and n2 are parametres which are placholder
    print("n1: ",n1)
    print("n2: ",n2)
    return sum

#positional argument
# print("the sum is",add(2,3)) 

#keyword argument(named argument)
# print("the sum is",add(n2=5,n1=6)) 

#defaults argument
# print("the sum is",add(3)) 


#arbitrary argument
def addAllNumbers(*args): #here args used when we dont know how many num we want to insert
    sum =0
    for i in args:
        sum +=i
    return sum

# output = addAllNumbers(1,2,3,4,5)
# print("the sum  is",output)

def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)

studentInfo(name="darshan p",age=18,city="gandhinagar")



