"""使用枚举类"""
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '==>', member, ',', member.value)
"""
Jan ==> Month.Jan , 1
Feb ==> Month.Feb , 2
Mar ==> Month.Mar , 3
Apr ==> Month.Apr , 4
May ==> Month.May , 5
Jun ==> Month.Jun , 6
Jul ==> Month.Jul , 7
Aug ==> Month.Aug , 8
Sep ==> Month.Sep , 9
Oct ==> Month.Oct , 10
Nov ==> Month.Nov , 11
Dec ==> Month.Dec , 12
"""
print(Month.Jan.value)  # 1


# 自定义类
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


for name, member in Weekday.__members__.items():
    print(name, '==>', member, ',', member.value)

print(Weekday.Mon)  # Weekday.Mon
print(Weekday.Mon.value)
print(Weekday(1))  # Weekday.Mon
print(Weekday['Mon'])  # Weekday.Mon


# 练习：把Student的gender属性改造为枚举类型，可以避免使用字符串：
@unique
class Gender(Enum):
    female = 0
    male = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


daming = Student('daming', Gender.male)
print(daming.gender.value)
