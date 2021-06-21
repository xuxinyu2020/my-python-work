from types import MethodType


# 新建类
class Student(object):
    pass


s = Student()
# 给实例绑定属性
s.name = 'Cindy'
print(s.name)


# 给实例绑定方法
def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)  # 给实例绑定方法
s.set_age(25)  # 调用实例方法
print(s.age)

s2 = Student()
# s2.set_age(25) #其他实例不能调用


# 给class绑定方法，在是所有实例中都可以使用
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s2.set_score(100)
print(s2.score)

# __slots__
class Teacher(object):
    __slots__ = ('name','age')

t1 = Teacher()
t1.name = 'xinyu'
t1.age = 18
# t1.score = 100 会报错

# __slots__对子类实例不起作用
class Mentor(Teacher):
    pass

m1 = Mentor()
Mentor.score = 100