# 多任务可以由多进程完成，也可以由一个进程内的多线程完成。
import threading
import time


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# 多线程锁的使用
balance = 0


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


lock = threading.Lock()


def run_thread(n):
    for i in range(20000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
                lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
