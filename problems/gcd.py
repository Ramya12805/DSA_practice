# Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
def gcd(x,y):
    gcd=1
    if x%y==0:
        return y
    for k in range(int(y/2),0,-1):
        if x%k==0 and y%k==0:
            gcd=k
            break
    return gcd
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
res=gcd(x,y)
print("Gcd is:",res)