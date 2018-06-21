
def calc(n):
    print (n)
    if int(n/2) > 0:
        return calc( int(n/2) )
    print("-->",n)

calc(11)

#明确的结束条件
#问题规模每递归一次都应该比上一次的问题规模有所减少
#效率低
