# exp = ["Life",10,'science',[3,5]]
# '''print(exp)
# emp_list=[]
# print(emp_list)'''

# '''print(exp[0])
# print(exp[3])
# print(exp[-1])'''

# print(exp[1:4])
# print(exp[1:-1])
# print(exp[0:2])

fruits=['mango','custard apple','banana']
print(fruits)
fruits.append('black berry')
# print("updated List: ",fruits)

fruits.insert(1,'kiwi')
# print("updated List: ",fruits)

veges = ['tomato','potato','oninon']
# print("veges: ",veges)
fruits.extend(veges)
# print("updated List: ",fruits)

fruits[1]='grapes'
fruits[6]='chilli'
# print("updated list: ",fruits)
fruits.remove('chilli')
print("updated List: ",fruits)
del fruits[1]
print("updated List: ",fruits)
del fruits[4:6]
print("updated List: ",fruits)
print(len(fruits))
for fruit in fruits:
    print(fruit)
pop_see=fruits.pop(3)
print("updated List: ",pop_see)
print("updated List: ",fruits)