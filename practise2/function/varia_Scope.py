#Local Scope

# def greet():
#     mess = "Hello"
#     print(mess)

# greet()


#Global Scope
# message = "Alert! This is voyager 1 is reporting"
# def scop():
#     print("Local msg: ",message)

# scop()
# print("Global: ",message)


#Local Scope
def greet():
    message="Hi"
    def inner():
        nonlocal message
        message = "Good morning"
        print("local",message)
    
    inner()
    print("outer",message)
greet()