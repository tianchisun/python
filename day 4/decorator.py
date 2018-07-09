#
# def foo():
#     print('in the foo')
#     bar()
#
# def bar():
#     print('in the bar')
#
# foo()

import time
def bar():
    time.sleep(3)
    print('in the bar')

'''
def test1(func):
    start_time=time.time()
    func()  #run bar
    stop_time=time.time()
    print('the func run time is %s' %(stop_time-start_time))
test1(bar)
'''

def test2(func2):
    print(func2)
    return func2
bar=test2(bar)
bar()  #run bar