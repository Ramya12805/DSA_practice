# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

# Sample value of n is 5

num=int(input("Enter an integer to expand: "))
num=str(num)
num1 =int(str(num+num))
num2 = int(str(num+num+num))
print("The expanded number is: ",int(num)+num1+num2)