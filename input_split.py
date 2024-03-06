li=[]
n=int(input())
while(n>0):
    command=input()
    operation=command.split()
    if(operation[0]=="insert"):
        li.insert(int(operation[1]),int(operation[2])) 
    
    elif(operation[0]=="remove"):
        li.remove(int(operation[1]))
    
    elif(operation[0]=="append"):
        li.append(int(operation[1]))
    
    elif(operation[0]=="print"):
        print(li)
    elif(operation[0]=="sort"):
        li.sort()
    elif(operation[0]=="pop"):
        li.pop()
    elif(operation[0]=="reverse"):
        li.reverse()
    n-=1













# # Function to process input lines and store unique values in a list
# def process_input_with_reinput(input_lines):
#     unique_values = set()
#     result_list = []

#     for line in input_lines:
#         while True:
#             # Split the input line using a comma as the delimiter
#             split_values = line.split(',')

#             # Check if there are enough elements in the split_values list
#             if len(split_values) == 2:
#                 # Extract and strip values
#                 value = split_values[0].strip()
#                 category = split_values[1].strip()

#                 # Check if the value is unique and the category is valid
#                 if value not in unique_values and category in ('H', 'N'):
#                     result_list.append((value, category))
#                     unique_values.add(value)
#                     break
#                 else:
#                     if value in unique_values:
#                         print(f"Value '{value}' is repetitive. Please enter a unique value.")
#                     if category not in ('H', 'N'):
#                         print(f"Category '{category}' is invalid. Please enter 'H' or 'N'.")
#                     line = input("Re-enter the input (e.g., 5,H): ")
#             else:
#                 print("Invalid input format. Please enter values in the format 'value,category'.")
#                 line = input("Re-enter the input (e.g., 5,H): ")

#     return result_list

# # Example inputs
# input_lines = []
# for i in range(5):
#     input_line = input()
#     input_lines.append(input_line)

# # Process the input lines with re-input
# result_list = process_input_with_reinput(input_lines)
# print("Processed Result List:", result_list)
