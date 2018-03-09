#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
def decorator(fn):
    def wrapper(*args,**kw):
        print('begin call')
        n=fn(*args,**kw)
        print('end call')
        return n
    return wrapper
@decorator
def now(x,y):
    return x+y
f=now(11,22)
print(f)