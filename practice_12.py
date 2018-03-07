#杨辉三角的简便方法（practice_11.py)
def triangles():
    l = [1]
    while 1:
        yield l
        l = [1] + [ l[n] + l[n+1] for n in range(len(l)-1) ]  + [1] 
q=triangles()
for i in range(10):
    print(next(q))