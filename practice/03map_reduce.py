"""高阶函数map/reduce练习"""
import re
from functools import reduce


def f(x):
    return x * x


# 计算列表每个元素的平方
r = map(f, [1, 2, 3, 4, 5, 6])
print(r)  # <map object at 0x0000018BFDB96208>
print(list(r))  # [1, 4, 9, 16, 25, 36]
# 将列表中所有数字转化成字符
r = map(str, [1, 2, 3, 4, 5, 6, 7])
print(list(r))  # ['1', '2', '3', '4', '5', '6', '7']


def g(x, y):
    return x + y


r = reduce(g, [1, 2, 3, 4, 5])
print(r)

"""构造一个把str转为int的函数"""


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    return reduce(fn, map(char2num, s))


print(str2int('13478'))  # 13478


# 练习1：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(s):
    return s.capitalize()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 练习2：Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def fn(x, y):
        return x * y

    return reduce(fn, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 练习三：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    str_list = s.split('.')

    def int_ex(x, y):
        return 10 * x + y

    def str2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    def float_ex(x, y):
        return 0.1 * x + y

    if len(str_list) == 2:
        # 字符中有小数点
        integer_part = reduce(int_ex, map(str2num, str_list[0]))
        float_part = 0.1 * (reduce(float_ex, map(str2num, str_list[1][::-1])))
        return integer_part+float_part
    else:
        # 字符中没有小数点
        integer=reduce(int_ex, map(str2num, str_list[0]))
        return integer


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
