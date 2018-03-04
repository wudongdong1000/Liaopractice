#一元二次方程求解
import math
def quadratic(a,b,c):
    det=b**2-4*a*c
    if det<0:
        print('该方程无解')
    elif det==0:
        print('该方程有一个解')
        x=-b/(2*a)
        print('该方程的解为',x)
    else:
        print('该方程有两个解')
        x1=(-b-math.sqrt(det))/(2*a)
        x2=(-b+math.sqrt(det))/(2*a)
        print('该方程的解为(%.1f,%.1f):'% (x1,x2))
print('方程的形式为ax^2+bx+c')
A=float(input('请输入a的值:'))
B=float(input('请输入b的值:'))
C=float(input('请输入c的值:'))
quadratic(A,B,C)
      
