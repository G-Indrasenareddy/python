# 4 types = try,except,finally,raise 

# fp = None
# try:
#     fp = open('user.txt','r') # this line is risky statement so use try

# except FileNotFoundError as err:
#     print(err)

# data = fp.read()
# print(data)  #Error name = FileNotFound Error




fp = None
try:
    fp = open('user.txt','r') # this line is risky statement so use try

except FileNotFoundError as err:
    fp = open('emp.txt','r')

data = fp.read()
print(data)  #Error name = FileNotFound Error