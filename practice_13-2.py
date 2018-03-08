#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
from functools import reduce
def str2float(s):
    n=len(s)-s.find('.')-1
    N=s.find('.')
    s=list(s)
    s.pop(N)
    dg={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,
    '7':7,'8':8,'9':9}
    def char2num(s):
        return dg[s]
    def fn(x,y):
        return x*10+y
    return (reduce(fn,map(char2num,s)))/(10**n)

print(str2float('5.56'))
