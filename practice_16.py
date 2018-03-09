#利用闭包返回一个计数器函数，每次调用它返回递增整数：
#生成器
def gen():
    i=1
    while i:
        yield i
        i=i+1
N=gen()
def createCounter():
    def counter():
        return next(N)
    return counter
f1=createCounter()
for i in range(1,10):
    print(f1())

#下面这样是不行的(可以将i改为s=[0],因为list可修改)
'''def CreateCounter():
    i=0
    def counter():
        i=i+1
        return i
    return counter
f1=createCounter()
for i in range(1,10):
    print(f1())
'''
'''因为内部函数不能修改外部变量
闭包的含义就是，调用内部函数，并且附带上外部变量
所以
第一种，s=0，s=s+1这种写法，每次调用内部函数，s都指向0这个数字对象
返回值就是1 1 1 1 1

然而写成 nonlocal s 或者 s=[0] 这两种情况时
前者把s声明成了非局部变量 
所以s=s+1就可以修改外部函数变量s的值
第一次调用，（内部函数，s=0），s+1,s=1,返回1
下一次调用，（内部函数，s=1），s+1,s=2,返回2
以此类推...

后者让外部变量s=[0]，每次调用内部函数，s都指向这个只有一个元素的list
牢记list是可变对象，s指向list这个关系在每次调用中是没有发生改变的
但是list内部第一个元素s[0]指向的数字在每次调用后已经加1了
第一次调用，（内部函数，s=[0]），s[0]+1,s[0]=1,返回1
下一次调用，（内部函数，s=[1]），s[0]+1,s[0]=2,返回2
（注意这里s还是指向原来的那个list，内部函数并没有改变外部变量s的指向）
以此类推...
'''