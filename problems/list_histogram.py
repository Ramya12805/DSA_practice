# Write a Python program to create a histogram from a given list of integers.
arr=[2,3,6,5]
for i in range(len(arr)):
    for j in range(arr[i]):
        print("@",end="")
    print("\n")