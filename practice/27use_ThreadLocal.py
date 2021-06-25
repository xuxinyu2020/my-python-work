"""多线程环境，局部变量传递"""
import threading

local_school = threading.local()


def process_stu():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_stu()


t1 = threading.Thread(target=process_thread, args=('Lining',), name='Thread-a')
t2 = threading.Thread(target=process_thread, args=('Daming',), name='Thread-b')
t1.start()
t2.start()
t1.join()
t2.join()

