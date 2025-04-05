# class Student:

   
#     def __init__(self,n,a,d): #inbuilt __init__
#         print("in init")
#         self.name=n
#         self.age=a
#         self.dept=d
    
#     def __str__(self):
#         return "Name is {},age is {} and dept is {}".format(self.name,self.age,self.dept)
    
# st1 = Student("darshan",18,"ICT")
# print(st1)
# ----------------------------------------------------------------------------------------
# class sportsperson:
#     def __init__(self,a,b,c,d):
#         print("hii here is my information")
#         self.name=a
#         self.sport=b
#         self.ball=c
#         self.ground=d

#     def __str__(self):
#         return "Name is {},sport is {},ball is {}, ground is {}".format(self.name,self.sport,self.ball,self.ground)
    
# sp1 = sportsperson("darshan","handball","8 size","near basketball court")
# print(sp1)
#----------------------------------(LAB8-1)----------------------------------------------------------
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

