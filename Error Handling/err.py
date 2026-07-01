# a = int(input("Enter the a: "))
# b = int(input("Enter the b: "))
# print(a+b)
# print(a/b)
# print("GM")
# Here program terminates abnormally

#Case-2
#Now we will write error handling for above the code

try:
    a = int(input("Enter the a: "))
    b = int(input("Enter the b: "))
    print(a+b)
    print(a/b)
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
print("GM")
# Here program terminates successfully as we used the error handling
