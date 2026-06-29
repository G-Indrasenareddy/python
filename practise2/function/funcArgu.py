# def add_num(a,b):
#     sum=a+b
#     print("sum: ",sum)

# add_num(3,4)

# def add_num(a,b):
#     sum=a+b
#     print("sum: ",sum)

# a = int(input("Enter the num: "))
# b= int(input("Enter the num: "))
# add_num(a,b)


# def add_num(a,b):
#     sum=a+b
#     print("sum: ",sum)

# a,b = map(int,input("Enter the 2 nums: ").split())
# add_num(a,b)


# def add_num(a,b):
#     return a+b

# a,b = map(int,input("Enter the 2 nums: ").split())
# sum = add_num(a,b)
# print("sum: ",sum)

#function Arguments with default values
def add_num(a=10 , b=20):
    sum = a+b
    print("sum: ",sum)

add_num(12,24)
add_num(a=3)
add_num()
add_num(b=30)
