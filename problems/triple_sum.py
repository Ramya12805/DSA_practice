# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
num1=int(input("Enter first num: "))
num2=int(input("Enter second num: "))
num3=int(input("Enter third num: "))
if num1==num2==num3:
    print("The result is: ",3*(3*num1))
else:
    print("The result is: ",num1+num2+num3)
    