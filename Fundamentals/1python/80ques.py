#Inherit class Person in class student. Demonstrate the use of super() and define a method
# to demonstrate method overriding
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print({self.name}, {self.age})

class Student(Person):
    def __init__(self, name, age, rollno):
        super().__init__(name, age)
        self.roll_no = rollno

    def display_info(self):
        super().display_info()
        print(self.roll_no)

person1 = Person("darshan", 18)
person1.display_info()

student1 = Student("ankit", 20, "XYZ")
student1.display_info()
