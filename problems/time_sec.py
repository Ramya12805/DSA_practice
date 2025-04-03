# Write a Python program to convert all units of time into seconds.
days=int(input("Enter the no of days: "))
hours=int(input("ENter the no of hours: "))
minutes=int(input("Enter the no of minutes: "))
seconds=int(input("Enter the no of seconds: "))
total=(days*3600*24)+(hours*3600)+(minutes*60)+seconds
print("Total time in seconds: ",total)