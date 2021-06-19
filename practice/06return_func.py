def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 闭包
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


print(calc_sum(1, 3, 5, 7))
f1 = lazy_sum(1, 3, 5, 7)  # 调用lazy_sum返回的是求和函数
f2 = lazy_sum(1, 3, 5, 7)
print(f1)
print(f2)
print(f1())
print(f2())

# 应用：利用闭包写计数器
def createCounter():
    container = [0]

    def counter():
        container[0] += 1
        return container[0]

    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
