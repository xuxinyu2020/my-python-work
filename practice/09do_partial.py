"""偏函数学习"""
import functools

print(int('890'))
print(int('1234', base=8))
int8 = functools.partial(int, base=8)
print(int8('2345'))

max100 = functools.partial(max, 100)
print(max(89, 23, 67))  # 89
print(max100(89, 23, 67))  # 100
