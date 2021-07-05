"""序列化练习"""
# pickle
import json
import pickle

d = dict(name='Bob', age=20, acore=80)
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
print(d)

# json
d = dict(name='Bob', age=20, acore=80)
print(json.dumps(d))


# JSON进阶
# class序列化和反序列化
class Student(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


s = Student('徐新宇', 20, 'female')


def stu2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'sex': std.sex
    }



print(json.dumps(s,default=stu2dict,ensure_ascii=False))  # {"name": "xuxin", "age": 20, "sex": "female"}
print(json.dumps(s,default=lambda obj:obj.__dict__,ensure_ascii=False)) #万能公式
# 反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
def dict2stu(d):
    return Student(d['name'],d['score'],d['age'])

print(json.loads(json_str,object_hook=dict2stu)) #<__main__.Student object at 0x000002063CC369E8>
