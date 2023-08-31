# Surface area of a Cylindar

# Measurements

print(" Input the following")
print("Enter PI measurements")
pi = float(input())
print("Enter the radius")
rad = int(input())
print(" Enter the Height")
height = int(input())

# SA of Closed Cylindar
# 2 pi r2 + 2pi dh
surf_area = 2 * (pi * rad * rad) + pi * (rad + rad)* height
print( " The surface Area is ", surf_area)

# Open Tank
# pi r2 + pi dh
open = (pi * rad * rad) + pi * (rad *2)* height
print(" The surface area of the tank is ", open)

# Pipe
# pi d h
pipe = pi * (rad *2) * height
print(" The surface area of the pipe is ", pipe)