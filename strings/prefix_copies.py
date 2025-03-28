# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
string = str(input("Enter a string: "))
n=int(input("Enter the number of times the first two characters be copied: "))
first_two=string[0]+string[1]
print(first_two*n)