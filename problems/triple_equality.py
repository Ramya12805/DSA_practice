# sum three given integers. However, if two values are equal, the sum will be zero.
x=int(input("Enter 1st nmuber: "))
y=int(input("Enter 2nd number: "))
z=int(input("Enter 3rd number: "))
if x==y or x==z or y==z:
    sum=0
else:
    sum=x+y+z
print("Sum of numbers is: ",sum)
