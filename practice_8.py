#practice_7.py的简便方法（递归思想）
def trim(s):
    if s == '':
        return s 
    elif s[0] == ' ':  #若最前面字符为空格，则继续将后面的字符串代入函数
        return trim(s[1:]) 
    elif s[-1] == ' ': #若最后面字符为空格，则继续将前面的字符串代入函数
        return trim(s[:-1])
    else:
        return s  #若最后面和最前面字符均非空格，则输出此时的字符串
print(trim(' hello world  ')=='hello world')
