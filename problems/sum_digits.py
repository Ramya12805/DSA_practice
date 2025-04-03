# Write a Python program to calculate sum of digits of a number.
num=int(input("Enter a number: "))
sumi=0
while num>0:
    r=num%10
    sumi+=r
    num=num//10
print("Sum of digits: ",sumi)