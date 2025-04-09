#user defined exception handling
#demosytrate the occurense of following error with code snippet
    #a)import error
    #b)Ioerror = input output error
    #c)Nameerror
    #d)ZeroDevisionError
# try :
#     import math
# except ImportError:
#     print("An error related to import Module")
# print("out of except")

# try :
#     import mod1
# except ImportError:
#     print("An error related to import Module")
# except IOError:
#     print("An error in file opening")
# try :
#     import math
# except NameError:
#     print(45/34)
# print("error")

# except ZeroDivisionError:
    
# print("out of except")


# try :
#     import file
#     fp = open("a.txt","r")
# except :
#     print("error")

#----------------------------------------------------------------------------------------#
#type error
#OS error
#EO Error

#1)type eroor
try :
    result = "Hello" + 42
except TypeError as e:
    print(f"TypeError: {e}")

#2)Os eror
import os

try:
    #try to remove a file that does not exist
    os.remove("non_existing_file.txt")
except OSError as e:
    print(f"")