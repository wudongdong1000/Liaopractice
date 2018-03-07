'''利用切片操作，实现一个trim()函数，去除
字符串首尾的空格，不能使用str的strip()
author:吴冬冬
'''
def trim(str):
    n=len(str)
    print(n)
    STR=list(str)
    if str==' '*n:
        result=''
#找到字符串开头和结尾不为‘ ‘的位置
    else:
        m=0
        p=0
        for j in range(0,n):
            if STR[j]!=' ':
                m=j
                break
            
        for k in range(-1,-n,-1):
            if STR[k]!=' ':
                p=k
                break
        result=str[m:n+p+1]
        print(str[m:n+p+1]) 
    return result
print(trim(' hello world ')=='hello world')
            
                



