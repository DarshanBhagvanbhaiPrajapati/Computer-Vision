import math
x=int(input("entre x:"))
y=int(input("entre y:"))
r=int(input("entre r:"))

z=math.sqrt((pow(x,2) + pow(y,2)))
if z == r:
    print("point lies on the circle")
elif z > r:
    print("point is outside the circle")
elif z < r:
    print("point is inside ")
