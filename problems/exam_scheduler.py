# Write a Python program to display the examination schedule. (extract the date from exam_st_date).

#Way 1
# date=eval(input("Enter the exam scheduled date: "))
# print("Exam date:",date[0],"/",date[1],"/",date[2])

# Way 2
exam_st_date=(11,12,2024)
print("The examination will start from : %i/%i/%i" % exam_st_date)