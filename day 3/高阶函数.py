
def add(x,y,f):
    return f(x)+f(y)

res = add(1,-7,abs)
print(res)