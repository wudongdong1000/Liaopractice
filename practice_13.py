#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字


#第一种用自带的capitalize函数
'''def normalize(name):
    return map(str.capitalize,name)
print(list(normalize(['adam', 'LISA', 'barT'])))
'''
#第二种自己写capitalize函数
def normalize(name):
    def capitalize(s):
        s=list(s.lower())
        s[0]=chr(ord(s[0])-32)
        s=''.join(s)
        return s
    return map(capitalize,name)
print(list(normalize(['adam', 'LISA', 'barT'])))
    
            
                
                

