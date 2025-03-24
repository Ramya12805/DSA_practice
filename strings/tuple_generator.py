# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

# Sample data: 3, 5, 7, 23

values = input("Enter comma separated integers: ")
list_num = values.split(",")
tuple_num=tuple(list_num)
print("List: ",list_num)
print("Tuple: ",tuple_num)