#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools
def metric(fn):
    def wrapper(*args,**kw):
        t0=time.time()
        result=fn(*args,**kw)
        print('%s executed in %.3f ms' % (fn.__name__,time.time()-t0))
        return result
    return wrapper
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y
f=fast(11,22)
print(f)
@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z
s=slow(11,22,33)
print(s)
