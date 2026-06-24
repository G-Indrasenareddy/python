a,b,c = map(int,input("Enter a,b and c: ").split())
num = [a,b,c]
num.sort(reverse=True)
print(*num)