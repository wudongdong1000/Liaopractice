#对函数fact(n)编写doctest并执行
def fact(n):
    '''
    Calculate !*2*...*n
    '>>>'后有以一空格

    >>> fact(1) 
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: "value" is invalid x
    '''
    if n <1:
        raise ValueError('"value" is invalid x')
    if n==1:
        return 1
    return n*fact(n-1)

if __name__=='__main__':
    import doctest
    doctest.testmod()
    
