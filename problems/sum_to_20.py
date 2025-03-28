# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
k=x+y
if k>=15 and k<=20:
    print(20)
else:
    print(k)