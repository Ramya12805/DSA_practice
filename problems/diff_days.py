# Write a Python program to calculate the number of days between two dates.
from datetime import date
f_date = date(2014,7,2)
l_date = date(2014,7,11)
diff = l_date - f_date
print(diff.days)