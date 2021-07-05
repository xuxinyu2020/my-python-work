"""操作文件系统和目录"""
import os

print(os.name)
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
# print(os.uname())
# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

print(os.environ)
print(os.environ.get('COMMONPROGRAMFILES'))  # C:\Program Files\Common Files

# 查看当前目录的绝对路径
print(os.path.abspath('.'))  # E:\python\my-python-work\practice
# 组合目录路径，注意不要直接拼接字符，以消除操作系统差异
newdir = os.path.join('E:\python\my-python-work\practice', 'test')
# 新建目录
# os.mkdir(newdir)
# 删除目录
# os.rmdir(newdir)
# 目录拆分
# 获取最后级别的文件名和目录名
print(os.path.split('/Users/michael/testdir/file.txt'))  # ('/Users/michael/testdir', 'file.txt')
# 得到文件扩展名
print(os.path.splitext('/Users/michael/testdir/file.txt'))  # ('/Users/michael/testdir/file', '.txt')
# 文件重命名
# os.rename('test.py','test_rename.py')
# 删除文件
# os.remove('test.txt')


# 列出当前目录下的所有目录
result = [x for x in os.listdir('.') if os.path.isdir(x)]
print(result)
# 列出当前目录下所有的py文件
result2 = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(result2)


# 练习：
# 1. 利用os模块编写一个能实现dir -l输出的程序

# 2. 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
# 解法1：
def search(string):
    """
    :param string: 要查找的关键字
    :return: 返回包含该关键字的文件名列表
    """
    result = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if string in file:
                result.append(os.path.join(root, file))
    return result


print(search('python'))


# 解法2：递归解法
def file_search(string, start_path, result_list=None):
    if result_list is None:
        result_list = []
    if os.path.isdir(start_path):
        file_list = os.listdir(start_path)
        for file in file_list:
            if string in file:
                result = os.path.join(start_path, file)
                result_list.append(result)
        for dir in file_list:
            file_search(string, os.path.join(start_path, dir), result_list)
    return result_list

print("解法2：",file_search('python','.'))