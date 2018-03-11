#把Student的gender属性改造为枚举类型，可以避免使用字符串：
from enum import Enum,unique
@unique
class Gender(Enum):
    Male=0
    Female=1


class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
a=Student('mike',Gender.Female)
if a.gender==Gender.Female:
    print('yes')