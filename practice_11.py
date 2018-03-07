'''生成器(generator)
杨辉三角，把每一行看做一个list，试写一个generator,
不断输出下一行的list
'''
def triangles():
    n=1
    L=[1]
    while True:
        yield L
        p=L.copy()
        n=n+1
        L.append(' ')
        L[n-1]=1
        if n>=3:
            for i in range(1,n-1):
                L[i]=p[i-1]+p[i]
p=triangles()       
for i in range(15):
    print(next(p))