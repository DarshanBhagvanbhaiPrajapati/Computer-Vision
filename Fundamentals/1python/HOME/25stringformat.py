#str.format() = optional method that gives users
#               more control when displaying output

# animal = "cow"
# item = "moon"

# print("the" +" "+ animal +" "+  "jumped over the "+" "+ item)
# print("the {} jumped over the {} ".format("cow","moon"))
#           #this {} (called set) will point to first value as in format and second will point to
#           #second one i.e moon
# print("the {1} jumped over the {0} ".format("cow","moon")) #indexes using
# print("the {item} jumped over the {animal} ".format(animal="cow",item="moon"))

# text = "the {} jumped over the {} "
# print(text.format(animal,item))

##  second part of code

name = "DARSHAN"

print("Hello,my name is {}".format(name))
print("Hello,my name is {:10}.Nice to meet you".format(name))
print("Hello,my name is {:<10}.Nice to meet you".format(name)) #value left alligned
print("Hello,my name is {:>10}.Nice to meet you".format(name)) #value right alligned
print("Hello,my name is {:^10}.Nice to meet you".format(name)) #centre alligned


#third part

number = 1000

print("the number  is {:.3f}".format(number))
print("the number is {:,}".format(number)) #output= 1,000
print("the number is {:b}".format(number)) #gives binary search of that number
print("the number pi is {:o}".format(number)) #display octal number
print("the number pi is {:x}".format(number)) #display hexadecimal
print("the number pi is {:e}".format(number)) #diaply in scientific notation e for lowercase and E for capital




