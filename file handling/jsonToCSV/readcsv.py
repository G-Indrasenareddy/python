#write a python script to read csv file and print all employee names
import csv
fp=open('emp.csv','r')
emp_data = list(csv.reader(fp))
print(emp_data)

for emp in list(emp_data[1:]):
    print(emp)