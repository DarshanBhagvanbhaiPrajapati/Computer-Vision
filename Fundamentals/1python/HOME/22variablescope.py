#scope = the region that a variable is recognized
#      a variablr is only available from inside the region it is created
#      a global and locally scoped versions of a variable can be created


name = "Darshan" #global scope (available inside and outsiide function)

def display_name():
    name = "Code"   #local scope (available only inside this function)
    print(name)

display_name() 
print(name)