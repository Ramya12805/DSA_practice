# Write a Python program to get the volume of a sphere with radius six.
from math import pi
radius = float(input("Enter the radius of the sphere: "))
volume = (4/3)*pi*(radius**3)
print("volume of the sphere is: ",volume)