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
'''别人更容易理解的方法
def triangles():
    max=0
    last=[]
    while max<=10:
        l=[]
        if last==[]:
            l=[1]
        else:
            for i in range(0,max+1):
                if i==0 or i==max:
                    l.append(1)
                else:
                    l.append(last[i-1]+last[i])

        yield l
        last=l
        max+=1
q=triangles()
for i in range(10):
    print(next(q))
'''