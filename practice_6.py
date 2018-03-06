#没搞太懂
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
 
#计算移动了多少步
move(4, 'A', 'B', 'C')
def f(n):
    if n==2:
        return 3
    return f(n-1)*2+1
print(f(4))

