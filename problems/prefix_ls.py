# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
string = str(input("Enter the string: "))
if string.startswith("ls"):
    print(string)
else:
    print("ls"+string)