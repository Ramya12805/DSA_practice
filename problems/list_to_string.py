# Write a Python program that concatenates all elements in a list into a string and returns it.
arr=[1,2,3,4]
string=""
for i in range(len(arr)):
    string+=str(arr[i])
print("The concatenated string is: ",string)