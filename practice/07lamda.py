"""匿名函数的使用"""
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))
f = lambda x: x * x
print(f)
print(f(5))

"""练习：改造函数"""
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
