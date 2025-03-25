# Write a Python program to count the number 4 in a given list.
size=int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    arr.append(int(input()))

#Way 1
c=0
for i in range(size):
    if arr[i]==4:
        c+=1
print("Number of times 4 repeated is: ",c)


# Way 2
print("Number of times 4 repeated in the list is: ",arr.count(4))