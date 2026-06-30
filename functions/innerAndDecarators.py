def login_req(func):
    def inner(name,status):
        if status!=True:
            print("Login Required")
        else:
            func(name,status)

    return inner

def index(name,status):
    print("Home page")
def product_page(name,status):
    print("Product Page")

@login_req #if not add this @login_req then output will be order page"
def order_page(name,status):
    print("order page")
@login_req
def profile_page(name,status):
    print("Profile Page")

index("RG",False)
product_page("RG",True)
order_page("RG",False)
profile_page("RG",False)