#keyword arg = arguments preceded by an identifier when we pass them to a function
#              the order of the arguments doesnt matter,unlike positional arguments
#              python knows the names of the arguments that our function receive

def hello(first,middle,last):
    print("hello " + first + " "+ middle+" " + last)

hello(last="code",first = "Bro",middle="Dude")  #give keyword according to order
