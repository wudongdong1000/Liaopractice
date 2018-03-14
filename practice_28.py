#请将本地一个文本文件读一个为str并打印出来
fpath=r'/home/wu/picture.png'

with open(fpath,'rb') as f:
    s=f.read()
    print(s)
    
    

