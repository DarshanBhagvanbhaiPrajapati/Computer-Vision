def g(x):
    def h():
       nonlocal x
       x = x + 1
       print('in g(): x =', x)
    h()
    return x
x = 3
z = g(x)
print("Value of z:", z)