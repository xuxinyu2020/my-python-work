class Myobject(object):
    def __init__(self):
        self.x = 19

    def power(self):
        return self.x * self.x


obj = Myobject()
# 测试对象的属性
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))  # 会报错

setattr(obj, 'y', 21)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
print(getattr(obj, 'z', 404))
print(hasattr(obj,'power'))
print(getattr(obj,'power'))
fn = getattr(obj,"power")
print(fn())
