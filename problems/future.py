# Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
amt=10000
rate= 3.5
years=7
future_value = amt*((1+(0.01*rate))**years)
print(round(future_value,2))