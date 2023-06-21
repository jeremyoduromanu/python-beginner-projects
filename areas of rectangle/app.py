length1 = int(input("Enter the length of the first rectangle :"))
length2 = int(input("Enter the length of the second rectangle: "))
width1 = int(input("Enter the width of the first rectangle: "))
width2 = int(input("Enter the width of the second rectangle: "))

areaOfRec1 = length1 * width1
areaOfRec2 = length2 * width2

if areaOfRec1 == areaOfRec2:
    print("The rectangles has the same area")
elif areaOfRec1 > areaOfRec2:
    print("The rectangle one has bigger area than rectangle two")
else:
    print("Rectangle 2 has bigger area")