# Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("The colors in list 1 not in list 2 are: ",color_list_1.difference(color_list_2))