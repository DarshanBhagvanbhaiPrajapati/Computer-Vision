def g(x):
    def h():
        x ='abc'
    x = x+1 #new variable in local scope
    print('in g(x): x =', x)
    h()
    return x

x=3 #in global scope
z=g(x)
