"""
read user.txt file and write data into emp.txt file
"""

fp1 = open('user.txt', 'r')
fp2 = open('emp.txt', 'w')

data = fp1.read()

fp2.write(data)

print("Data Written successfully")

fp1.close()
fp2.close()