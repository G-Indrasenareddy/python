num = int(input("Enter 3 digit num: "))
temp = num
count = 0
while temp!=0:
    temp = temp//10
    count = count+1

if count==3:
    print(f'{num} is 3 digit number')
else:
    print(f'{num} is not 3 digit number')