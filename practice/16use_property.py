# class Student(object):
#
#     def get_score(self):
#         return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError("score must be integer!")
#         if value < 0 or value > 100:
#             raise ValueError("score must between 0~100")
#         self._score = value
#
# s=Student()
# s.set_score(101)
# print(s.get_score())

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0~100")
        self._score = value

s=Student()
s.score=100 #实际转化为s.set_score(60)
print(s.score)#  实际转化为s.get_score()

# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
    @property
    def width(self):
        return self.__witdth

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self,value):
        self.__width = value

    @height.setter
    def height(self,value):
        self.__height = value

    @property
    def resolution(self):
        return self.__height* self.__width
    
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')