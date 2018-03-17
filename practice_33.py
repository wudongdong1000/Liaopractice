#请尝试写一个验证Email地址的正则表达式。
import re
import time 
def is_valid_email(addr):
    m=re.match(r'^(\<([a-zA-Z\s]+)\>\s*)?([a-zA-z\.]+)@([a-zA-Z]+).(com|org)$',addr)
    print('开始匹配...')
    time.sleep(2)
    if m:
        print('匹配成功')
        if m.group(1):
            print(m.group(2)) 
        else:
            print(m.group(3))
    else:
        print('不匹配')

is_valid_email('someone@gmail.com')



