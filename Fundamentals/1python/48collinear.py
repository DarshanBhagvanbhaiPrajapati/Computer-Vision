coordinate_x1=int(input("entre the x1: "))
coordinate_y1=int(input("entre the y1: "))

coordinate_x2=int(input("entre the x2: "))
coordinate_y2=int(input("entre the y2: "))

coordinate_x3=int(input("entre the x3: "))
coordinate_y3=int(input("entre the y3: "))

slope1 = (coordinate_y2-coordinate_y1) / (coordinate_x2-coordinate_x1)
slope2 = (coordinate_y3-coordinate_y2) / (coordinate_x3-coordinate_x2)

if(slope1 == slope2):
    print("collinear line")
else:
    print("line are not collinear")
    