# enames = {"rahul", "sonia", "pg", "modi", "sonia"}
#union
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.union(s2))
print(s1 | s2 )

print(s1.intersection(s2))
print(s1&s2)

print(s1.difference(s2))
print(s1-s2)

print(s1.symmetric_difference(s2)) 
print(s1^s2)

s3={30,50,62,25,35}
print(sorted(s3))