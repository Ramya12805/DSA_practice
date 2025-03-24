# Write a Python program that calculates the area of a circle based on the radius entered by the user.

#Way 1
# radius=float(input("Enter the radius of the circle: "))
# area=3.14*radius*radius
# print("Area of the cirlce is : ",area)

#Way 2
from math import pi
radius=float(input("Enter the radius of the cirlce: "))
area = pi * radius**2
print("Area of the cirlce is: ",area)