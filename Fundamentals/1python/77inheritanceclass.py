class Person:
    def __init__(self,i,fn,ln):
        print("construction of parent class")
        self.Pid=i
        self.fname=fn
        self.lname=ln

    def disp_details(self):
        print(self.Pid,self.fname,self.lname)

class Employee(Person):
    def __init__(self,i,fn,lname,sal):
        print("constructor of child class")

        super().__init__(i,fn,lname) #this will call the cinstructor for parent class
        self.salary=sal
    def disp_details(self):
        #super().disp_details()    #function overriding when only both have same name ,
                                    #same parametres,but one in poarent and one isin child
        print("salery:",self.salary) 

e1 = Employee(1,'ABC','XYZ',10000000)
e1.disp_details()

#OOPS
#class and object
# 1)Encapulation == Data hiding
# 2)INheritence(base case and deriverd class)
# 3)Polymorphism = Funciton Overriding (it related with same name) ,while in c++ function overloading,
#overriding,and operatiors


