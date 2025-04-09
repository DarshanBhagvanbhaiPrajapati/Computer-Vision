#lab9:Create two classes “Cat” and “Dog” with two attributes “name” and “age”. 
#     Both classes share a similar structure and have the same method names info() and make_sound().
#     When a make_sound() is called using dog object it should print “Bark”, and when called using cat object, it should print “Meow”.
#     Similarly, when info() is called using dog object it should print “I am a dog. My name is $dog_name$. I am $dog_age$ years old.

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        print("Meow")
    
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        print("Bark")
    
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

# Creating instances of the classes
cat1 = Cat("Betty", 3)
dog1 = Dog("Charlie", 5)


cat1.make_sound()  # Output: Meow
dog1.make_sound()  # Output: Bark

cat1.info()  # Output: I am a cat. My name is Whiskers. I am 3 years old.
dog1.info()  # Output: I am a dog. My name is Buddy. I am 5 years old.


