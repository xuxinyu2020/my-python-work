"""廖雪峰decorator"""
import functools
import time


def log(text):
    def decortor(func):
        @functools.wraps(func)  # 使用这个装饰器，可以将原来函数的名字复制到__name__
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decortor


# 函数对象可以赋值给变量
@log('execute')
def now():
    print('2021-6-20')


# f = now
# f()
print(now.__name__)
# print(f.__name__)

now()

"""练习：请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间："""


def metric(fn):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print('%s executed in %s ms' % (fn.__name__, t2 - t1))
        return result

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print("测试成功！")

"""练习：请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。"""
"""思考：装饰器无论带不带参数都支持"""

def log(info='execute'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if info == "":
                print(f"begin call")
                func(*args, **kwargs)
                print(f"end call")
            else:
                print(f"{info} begin call")
                func(*args, **kwargs)
                print(f"{info} end call")

        return wrapper
# 关键代码解释：如果装饰器带参数，那么传入的参数就是字符串，那么就就是不可callable的
#     如果装饰器不带参数，那么传入的参数就是函数名称，那么就可以callable
    if callable(info):
        return decorator(info)
    else:
        return decorator

# 装饰器带参数和不带参数均可
@log('sysinfo:')
def f():
    pass

# @log
# def f():
#     pass

f()
