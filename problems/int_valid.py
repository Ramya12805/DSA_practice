# Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
x=int(input("Enter 1st integer: "))
y=int(input("Enter 2nd integer: "))
if not(isinstance(x,int) and isinstance(y,int)):
    print("Entered integers are not integers.")
print(x+y)