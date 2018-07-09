'''
生成器   只有在调用时才会生成相应的数据
只记录当前位置
只有一个 _next_() 方法
( i*i for i in range(10) )
'''

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        #print(b)
        yield b
        a,b = b,a+b
        n = n+1
    return '---done---'

f=fib(7)
while True:
    try:
        x=next(f)
        print('f:',x)
    except StopIteration as e:
        print('',e.value)
        break

# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())