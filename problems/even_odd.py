# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
num=int(input("Enter an integer: "))

#Way 1
# if num%2==0:
#     print("Number is Even")
# else:
#     print("Number is Odd")

#Way 2
# if num&1 == 0:
#     print("Number is Even")
# else:
#     print("Number is Odd")

#Way 3
# if (num//2)*2==num:
#     print("Number is even")
# else:
#     print("Number is Odd")

#Way 4
def even_odd(n):
    if n==0:
        return "Even"
    elif n==1:
        return "Odd"
    return even_odd(n-2)
print(even_odd(num))