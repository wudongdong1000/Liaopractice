#请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.set_gender(gender)
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if gender.title()=='Male' or 'Female':
            self.__gender=gender
        else:
            raise ValueError('wrong value')
mike=Student('Mike','Female')

print(mike.get_gender())
mike.set_gender('male')
print(mike.get_gender())