exg = ('Mango','Banana','Orange','Mango')
print(exg)
print(exg[1])
# exg[2] = 'Grapes' #This will give an error because tuples are immutable
# print(exg)
print(len(exg))
for fruit in exg:
    print(fruit)

print(exg.count('Mango'))

mess = "hi who are you"
print(mess)