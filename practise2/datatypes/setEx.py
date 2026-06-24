# eid = {120,154,160,170}
# ename={"Rahul Gandi","Narendra Modi","Amit Shah","Sonia Gandhi"}
# mixed ={'a','like',150,'Rahul Gandi'}
# print(eid)
# print(ename)
# print(mixed)

# empty_set = set()
# empty_dic= {}
# print(type(empty_set))
# print(type(empty_dic))


# # print(eid[0]) #This will give an error because sets are unordered and unindexed

# ename.add("Yogi Adityanath")
# print(ename)

# tupleExp=('Train','Bus','aeroplane','ship')
# ways={'track','road','air','water'}
# ways.update(tupleExp)
# print(ways)
# mixed.discard('Rahul Gandi')
# print(mixed)
# # print(sum(ename)) #This will give an error because sum() function is not applicable on set of strings
# for led in ename:
#     print(led)


set1={10,20,30,40}
set2={30,40,50,60}

print(set1.union(set2))
print(set1 | set2)

print(set1.intersection(set2))
print(set1 & set2)

print(set1.difference(set2))
print(set1-set2)

print(set1.symmetric_difference(set2))
print(set1^set2)

print(set==set2)