#偏函数
import functools
def www(x,r=2,z=4):
    y=x+r+z
    return y 
kw={'r':4,'z':4}
www1=functools.partial(www,**kw)
a=www(1)
print(a)
b=www1(3)
print(b)
