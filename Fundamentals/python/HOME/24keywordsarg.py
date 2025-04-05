# **kwargs = parameters that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword 
#            arguments

def hello(**kwargs):
    # print("HIIII" +" "+ kwargs['first'] + " "+ kwargs['last'])
    print("heloooooo")
    for key,value in kwargs.items():
        print(value)

hello(first = "darshan",middle="ankit",last="jaimin")
