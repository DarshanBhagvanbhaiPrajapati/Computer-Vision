file = open("input.txt",'r') #if i will not write 'r' then it also print because it is default mode

print(file)
text = file.read()
print(text)
file.close()  #this will read file

# file = open("input.txt",'w')
# file.write("hii awesome that is!")
# file.close()

# file = open("input.txt",'a') #append this
# file.write("hii awesome that is!")
# file.close()


# with open('input.txt','a') as file: #with function we do not have to close 
#     file.write("hey i am there")
#--------------------------------(READ)------------------------------------------------------
# file = open("input.txt","r")

# data = file.read(5) #will read only first 5 letters
# line1 = file.readline() #will read line at a time
# print(line1)

# line2 = file.readline()
# print(line2)
# file.close()
#--------------------------------(write=over write),(append=add at the end)-----
# file = open("input.txt","w")

# file.write("edit this in my file,64")

# file.close()#this will over right edit this in my file6446
#(APPEND)
# file = open("input.txt","a")

# file.write("\nHOW ARE YOU")

# file.close()#this will  add at end 





