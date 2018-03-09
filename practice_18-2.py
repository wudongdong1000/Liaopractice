'''思考一下能否写出一个@log的decorator，使它既支持：
@log
def f():
    pass
又支持：
@log('execute')
def f():
    pass
'''
def log(s='execute'):
    def decorator(fn):
        def wrapper(*args,**kw):
            print('%s %s' % (s,fn.__name__))
            return fn(*args,**kw)
        return wrapper
    return decorator

#测试

@log()
def f():
    return 'hello'
f=f()
print(f)
@log('try')
def f1():
    return 'hello'
f=f1()
print(f)
