'''请利用@property给一个Screen对象加上width和height属性，
以及一个只读属性resolution：
'''
class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError('width must be  integer or float')
        if value<0:
            raise ValueError('value must >0')
        self.__width=value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError('width must be  integer or float')
        if value<0:
            raise ValueError('value must >0')
        self.__height=value
    @property
    def resolution(self):
        return self.__width*self.__height
s=Screen()
s.width=2
s.height=20
print(s.resolution)
        
        