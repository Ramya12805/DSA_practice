arr=[1,2,3,4,5]
element=int(input("Enter the number to find: "))
for i in range(len(arr)):
    if arr[i]==element:
        print("Element found at the index : ",i)