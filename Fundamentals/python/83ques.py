#lab 9:Explain the concept of multiple Inheritance with suitable example.

class Class1:
	def m(self):
		print("In Class1") 
	
class Class2(Class1):
	pass

class Class3(Class1):
	def m(self):
		print("In Class3") 
	
class Class4(Class2, Class3):
	pass	

obj = Class4()
obj.m()
