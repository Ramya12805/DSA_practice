# Write a Python program to test whether a passed letter is a vowel or not.
letter = str(input("Enter a character: "))

#Way 1
vowels = ['a','e','i','o','u']
if letter in vowels:
    print("The entered letter is a vowel")
else:
    print("The entered letter is not a vowel")

