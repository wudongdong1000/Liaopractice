'''为了统计学生人数，可以给Student类增加一个类属性，
每创建一个实例，该属性自动增加：
'''
class Student(object):
    count = 0
    def __init__(self,name):
        self.name=name
        Student.count=Student.count+1
print(Student.count)
a=Student('mike')
print(Student.count)
b=Student('json')
print(Student.count)
c=Student('jack')
print(Student.count)