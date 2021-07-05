"""多进程"""
# multiprocessing
import os
import random
import subprocess
import time
from multiprocessing import Process, Pool,Queue


def run_proc(name):
    print("Run child process %s(%s)" % (name, os.getpid()))


# if __name__ == '__main__':
#     print("父进程：%s" % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('即将开始子进程')
#     p.start()
#     p.join()
#     print('子进程结束！')

# Pool用法
def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(3)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('等待所有子进程执行完毕')
#     p.close()
#     p.join()
#     print('所有子进程处理完毕')

# 子进程
# subprocess
# print('$ nslookup 114.114.114.114')
# r = subprocess.call(['nslookup','114.114.114.114'])
# print('Exit code',r)

# commuicate()方法
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'114.114.114.114\n')
print(output.decode('utf-8', errors='ignore'))
print('Exit code:', p.returncode)


# 进程间通讯
def write(q):
    print('Process to write:%s' % os.getpid())
    for value in ['a', 'b', 'c']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
