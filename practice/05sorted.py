print(sorted([35, -2, 9, 45, 1, 12]))
print(sorted([35, -2, 9, 45, 1, 12], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# 学生姓名成绩排序，分别以姓名和成绩排名
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


def by_grade(t):
    return t[1]


L1 = sorted(L, key=by_name)
L2 = sorted(L, key=by_grade)
print(L1)
print(L2)