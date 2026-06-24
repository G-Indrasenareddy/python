english = ['zero','one','two','three','four',
           'five','six','seven','eight','nine']
num = int(input("Enter the single digit: "))
if 0<= num <=9: 
    print(english[num])
else:
    print("Invalid syntax")