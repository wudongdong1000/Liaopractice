import base64
'''def safe_base64_decode(s):
    l=len(s)%4
    b=s.decode('ascii')
    if l==0:
        return base64.b64decode(s)
    elif l==1:
        return base64.b64decode(b+'=')
    else:
        return base64.b64decode(b+'==')
#bac=base64.b64decode(b'abcd')
print(safe_base64_decode(b'YWJjZA'))
'''
#别人的方法
def safe_base64_decode(s):
    return base64.b64decode(s+len(s)%4*b'=')

print(safe_base64_decode(b'YWJjZA'))

    