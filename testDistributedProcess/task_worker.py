import _queue
import time
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


if __name__ == "__main__":
    # 由于这个QueueManager只从网络上获取Queue，所以注册时候只提供名字
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    # 连接到服务器
    server_addr = '127.0.0.1'
    print('Connect to server %s...' % server_addr)
    m = QueueManager(address=(server_addr, 5000), authkey=b'abc')

    # 连接
    m.connect()

    # 获取Queue对象
    task = m.get_task_queue()
    result = m.get_result_queue()

    # 从task队列取任务，把结果写入result队列
    for i in range(9):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d...' % (n, n))
            r = '%d * %d = %d' % (n, n, (n * n))
            time.sleep(1)
            result.put(r)
        except _queue.Empty:
            print('task queue is empty.')

    # 处理结束
    print('worker exit.')
