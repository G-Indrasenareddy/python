#decarator means
# def division(a,b):
#     print(a/b)
# print("Hello world")

# division(10,5) # op== 2
# division(10,0) # zero divivsion error if not used meta function



# now usage of decarator
from smart import smart_div
@smart_div
def division(a,b):
    print(a/b)
print("Hello world")

division(10,5) # op== 2
division(10,0) # zero divivsion error if not used meta function