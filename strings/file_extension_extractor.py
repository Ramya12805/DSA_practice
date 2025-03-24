# Write a Python program that accepts a filename from the user and prints the extension of the file.

# Sample filename: abc.java

filename = input("Input the filename: ")
file_extension = filename.split(".")
print("The extension of the file is: ",repr(file_extension[-1]))