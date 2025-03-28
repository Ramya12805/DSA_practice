#  to find the least common multiple (LCM) of two positive integers.
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))

if(x>y):
    z=x
else:
    z=y
while True:
    if(z%x==0) and (z%y==0):
        lcm=z
        break
    z+=1

print("Lcm between two number is: ",lcm)