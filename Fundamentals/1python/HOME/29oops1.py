#oops = to map with real world scenerio,we started using objects in code.
#       here main focus is on objects/data not on functions!
#classes-- user defined datatypes,blueprint/templet for objects
#object-- instance of type class ,mimmic real world entities
#due to function redundancy decrease and reusability increase
#----------------------------------------------------
# class Student: #this is class
#     name = "darshan prajapati"

# s1 = Student() #this is object
# print(s1.name)

#----------------------------------------------------

# class Sportsman:
#     game = "Handball"
#     region = "pune"

# S1 = Sportsman()
# print(S1.game)
# print(S1.region)

#-----------(CONSTRUCTOR)-----------------------------
# class Student: #this is class
#     # #1)default construction
#     # def __init__(self): 
#     #    pass  

#     #2)parameterized constructors
#     def __init__(self,name,marks):
#         self.name = name #WE ARE DEFFINING NAME FOR OBJECT
#         self.marks = marks
#         print("adding new student in database!")

# s1 = Student("Darshan",100) #this () is passing into __init__ and call that 
# print(s1.name,s1.marks) #we will get darshan

# s2 = Student("PRAJAPATI",98)
# print(s2.name,s2.marks)  #ATTRIBUTES: data or variable we ue in this called 

#---------------(ATTRIBUTES)-----------------------------
#1)CLASS AND INSTANCE ATTRIBUTES
#class:jo chiz common hoti he usko ham ek bar likhtehe
#instance:jo different ho sabke liye(jese name,roll no ,marks etc)

# class Student: 
#     college_name = "PDEU" #class ATTRIBUTES
#     name = "XYZ" #class ATTRIBUTES
#     def __init__(self,name,marks):
#         self.name = name  #object attr precedence > class attr precedence
#         self.marks = marks
#         print("adding new student in database!")

# s1 = Student("Darshan",100) 
# print(s1.name,s1.marks) 

# print(Student.college_name)

# print(s1.name)

#----------------(METHODS) ----------------------------------
#methods are functions that belong to objects
# class Student: 
#     college_name = "PDEU"
#     def __init__(self,name,marks):
#         self.name = name  
#         self.marks = marks

#     def welcome(self):
#         print("welcome to PDEU😇",self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("Darshan",100) 
# s1.welcome()
# print(s1.get_marks())

#--------------------------------------------------------------
#Q) create student class that takes name and marks of three subject as argument in constructor 
    #then create a method to print the average
# class student:
#     def __init__(self,name,marks): #constructor ,marks as list ex=[80,90]
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for value in self.marks:
#             sum += value
#         print("hii your avg score is:",sum/3)

# s1=student("darshan",[90,99,100])
# s1.get_avg()

#------------------------(ABSTRACTION,ENCAPSULATION--------------------------------------------
#in oops mainly 4 :1)ABSTRACTION,2)ENCAPSULATION,3)INHERITANCE,4)POLYMORPHISM
#1)ABSTRACTION:HIDING THE IMPLEMENTATION DETILS OF A CLASS AND ONLY SHOWING THE ESSENTIAL FEATURES TO THE USER
#2)ENCAPTULATION: wrapping data and functions into a single unit(object).
 
#Q)create account class with 2 attributs - balance and accounts:
  #create methods for debit,credit and printing the balance

class Account:
    def __init__(self,bal,account ):
        self.balance = bal
        self.account_no = account  

    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance= ",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance= ",self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(500) 
acc1.credit(40000)
acc1.debit(10000)

















