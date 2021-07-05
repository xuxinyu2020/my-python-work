"""错误处理"""
# try的处理逻辑
import logging

try:
    print("try...")
    r = 10 / int('1')
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
except ValueError as e:
    print('except:', e)
else:
    print('No error!')
finally:
    print('finally...')
print('END')

# 记录错误

# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# print("-------loging-----------")
# main()
# print('END')


# 练习：
from functools import reduce


def str2num(s):
    return int(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)
    except ValueError as e:
        print('except:', e)


main()
