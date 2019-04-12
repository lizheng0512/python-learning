import _queue
import queue
import random
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass


if __name__ == "__main__":
    # 把两个Queue注册到网络上，callable来关联Queue对象
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    # 绑定端口，设置密码abc
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue
    manager.start()
    # 获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put Task %d...' % n)
        task.put(n)
    print('Try get results...')
    for i in range(10):
        try:
            r = result.get(timeout=10)
            print('Result: %s' % r)
        except _queue.Empty:
            print('result queue is empty.')

    # 关闭
    manager.shutdown()
    print('master exit...')
