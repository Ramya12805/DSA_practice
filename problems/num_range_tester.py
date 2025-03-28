# Write a Python program to test whether a number is within 100 of 1000 or 2000.
num=int(input("Enter a number: "))
if num<=100:
    print("The given number is less than 100")
elif num>100 and num<=1000:
    print("THe given number is in between 100 and 1000")
elif num>1000 and num<=2000:
    print("The given number is in between 1000 and 2000")
else:
    print("The given number is greater than 2000")