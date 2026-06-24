a,b,c = map(int,input("Enter the a,b and c: ").split())
if a>b and a>c :
    print(f'{a} is greater')
elif b>a and b>c:
    print(f'{b} is greater')
elif c>a and c>b:
    print(f'{c} is greater')