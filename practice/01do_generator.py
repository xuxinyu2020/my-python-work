"""利用生成器输出杨辉三角"""
def triangle(height):
    """height:三角形高"""
    n = 0
    result = [1]
    while n < height:
        yield result
        list, result = result, []
        l = len(list)
        a = 0
        for i in range(l):
            b = list[i]
            a, b = b, a + b
            result.append(b)
        a, b = 0, list[-1]
        a, b = b, a + b
        result.append(b)
        n += 1
    return 'done'


g = triangle(10)
while True:
    try:
        print(next(g))
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
