# Write a Python program to calculate the hypotenuse of a right angled triangle.
import math
side1=int(input("Enter the length of side1: "))
side2=int(input("Enter the length of side2: "))
hyp=math.sqrt(side1**2+side2**2)
print("Hypotenuse of the right angle triangle: ",hyp)