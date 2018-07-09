import time

user,passwd = 'stc','123qwe'

def auth(auth_type):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if auth_type == "local":
                username = input("username:").strip()
                password = input("password:").strip()
                if user == username and passwd == password:
                    print("succes")
                    res = func(*args, **kwargs)   #from home
                    print("----after authenticaion")
                    return res
                else:
                    exit("faild")
            elif auth_type == "ldap":
                print("不会ldap")
        return wrapper
    return outer_wrapper


def index():
    print("welcome to index")

@auth(auth_type="local")
def home():
    print("welcome to home")
    return "from home"

@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs")

index()
home()
bbs()