#to find voume of cube, cylinder, rectangular box 
#cube
s = int(input("Enter side: "))
vol_cube = s*s*s
print("Volume of Cube: ",vol_cube)
#cylinder 
r = int(input("Enter radius: "))
h = int(input("Enter height: "))
vol_cyl = 3.14*r*r*h
print("Volume of cylinder: ", vol_cyl)
#rectangle 
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
he = int(input("Enter height: "))
vol_rect = l*b*he
print("Vulume of rectangular box: ",vol_rect)