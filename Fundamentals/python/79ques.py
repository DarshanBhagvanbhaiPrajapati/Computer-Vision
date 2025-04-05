#Q)WAP with class Person definition. Demonstrate the use of following concepts of object
   #oriented python through your program.* Object creation* encapsulation* _init_()_str_()

class person:
    def __init__(self,a,b,c):
        print("hii here is my information")
        self.name=a
        self.branch=b
        self.roll_no=c

    def __str__(self):
        return "Name is {},branch is {},roll_no is {}".format(self.name,self.branch,self.roll_no)
    
p1 = person("xyz","ict","23BITXYZ")
print(p1)