#计算若干个数的积
def product(*numbers):
    if not numbers:
        
        return '请输入值'
    pro=1
    for i in numbers:
        pro=pro*i
    
    return pro
print(product(*map(int,input('请输入数值，用空格隔开:').split())))

