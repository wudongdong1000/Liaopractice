from io import StringIO
s=StringIO()
s.write('hello world')
print(s.tell())
s.seek(0,0)
print(s.tell())
print(s.read())