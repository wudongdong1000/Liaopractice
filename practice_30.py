'''编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，
并打印出相对路径。
'''
import os 
def findstr(path,s):
    for i in os.listdir(path):
        if s in i:
            print(i)
        if os.path.isdir(i):
            findstr(os.path.join(path,i),s)
findstr(os.path.abspath('.'),'py')

#别人的


'''import os

def findStr(p, w):

    for x in os.listdir(p):
        p1 = os.path.join(os.path.abspath(p),x)
        if w in x:
            print(p1)

        if os.path.isdir(p1):
            findStr(p1, w)
findStr(os.path.abspath('.'),'py')
'''