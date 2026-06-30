'''
Decarator is function, it takes function as argument
and modify the functionality and return
'''

def smart_div(func):

    def inner(a,b):
        if b==0:
            print("cannot divide by zero")
        else:
            return func(a,b)
    return inner