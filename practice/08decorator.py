# 装饰器
"""特点：
1.函数A作为参数，函数B接受函数A的名称作为参数
2.有闭包特点
"""


# 简单例子
# 函数作为参数
def func(f):
    print(f)
    f()
    print("---------->func")


def test():
    print("---------->test")


func(test)


# ---------->test
# ---------->func

# 定义简单的装饰器
# 执行过程：
# 1. house作为被装饰函数
# 2. 将被装饰函数做欸参数传给装饰器decorte
# 3. 执行decorate函数，返回值传给house
# def decorate(func):
#     print("wrapper外层打印")
#
#     def wrapper():
#         print("开始打地基")
#         func()
#         print("开始装修天花板")
#
#     print("wrapper外层打印结束")
#     return wrapper
#
#
# @decorate
# def house():
#     print("我建造了一座房子")


# house()  # 我建造了一座房子

# house()
# print(house)  # <function decorate.<locals>.wrapper at 0x0000019923CC4598>


# 万能装饰器

# 1. 接收函数的参数
def decorate(func):
    print("wrapper外层打印")

    def wrapper(*args, **kwargs):
        print("开始打地基")
        func(*args, **kwargs)
        print("开始装修天花板")

    print("wrapper外层打印结束")
    return wrapper


@decorate
def house(num, location="陆家嘴"):
    print("我建造了{}座房子，位置在{}".format(num, location))


house(200, location="深圳")


# 2. 接收装饰器的参数
def work(num):
    print('--------1')
    def inner_func(func):
        print('--------2')
        def wrapper(*args, **kwargs):
            print('--------3')
            print("完成了{}张卷子".format(num))
            func(*args, **kwargs)

        return wrapper

    return inner_func


@work(10)
def homework(subject):
    print(homework)
    print("完成了{}的作业".format(subject))


homework('语文')


# 多层装饰器
# 执行顺序：由上到下

def set1(func):
    print("1 start")

    def wrapper():
        print("准备准考证")
        func()

    print("1 end")

    return wrapper


def set2(func):
    print("2 start")

    def wrapper():
        print("准备纸笔")
        func()

    print("2 end")
    return wrapper


@set2
@set1
def exam():
    print("正在考试中")


exam()
