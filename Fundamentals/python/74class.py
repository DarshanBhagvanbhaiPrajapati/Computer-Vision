#part of oops

class Student:
    """this is a student """

    #constructor ---->> used to initialize the object , generally two types
    #1)default
    #2)parametterized
    def __init__(self,roll,name,marks,add): #inbuilt __init__
        self.roll=roll  #properties
        self.name=name
        self.marks=marks 
        self.add=add
    
    def s_info(self):
        print("roll:",self.roll)
        print("name:",self.name)
        print("marks:",self.marks)
        print("add:",self.add)

#create a object
s1 = Student('64','darshan prajapati',100,'gandhinagar,saragasan')
s1.s_info()

