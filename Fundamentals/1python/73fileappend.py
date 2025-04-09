file = open("input.txt","w")
file.write("see you soon!")
file.close()
file = open("input.txt","r")
print(file.readlines()) #readlines means it return list if only readline it will diff
