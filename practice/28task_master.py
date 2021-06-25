import queue
import random
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

def task_queue_func():
    global task_queue
    return task_queue


def result_queue_func():
    global result_queue
    return result_queue


class QueueManager(BaseManager):
    pass

if __name__ == '__main__':
    QueueManager.register('get_task_queue', callable=task_queue_func)
    QueueManager.register('get_result_queue', callable=result_queue_func)

    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d' % n)
        task.put(n)

    print('Try get results..')
    try:
        for i in range(10):
            r = result.get(timeout=10)
            print('Result:%s' % r)
    except queue.Empty:
        print('Result queue is empty!')
    finally:
        manager.shutdown()
    print('manager exit.')
