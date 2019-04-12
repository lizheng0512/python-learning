"""
    python 内置的 collections 模块示例
"""
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter


# 利用OrderedDict实现一个FIFO的dict，当容量超出限制，先删除最早的key
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        contains_key = 1 if key in self else 0
        if len(self) - contains_key >= self._capacity:
            last = self.popitem(last=False)
            print('remove ', last)
        if contains_key:
            del self[key]
            print('set ', (key, value))
        else:
            print('add ', (key, value))
        OrderedDict.__setitem__(self, key, value)


if __name__ == "__main__":
    # namedtuple是一个函数，用来创建tuple的子类，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
    Point = namedtuple('point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x, p.y)
    # deque是高效实现了插入和删除的双向列表，适合用于队列和栈
    dq = deque([1, 2, 3, 4, 5])
    dq.append(6)
    dq.appendleft(0)
    print(dq)
    dq.remove(3)
    print(dq)
    dq.insert(3, 3)
    print(dq)
    # defaultdict是当key不存在时给出默认值的dict
    dd = defaultdict(lambda: 'default-value')
    dd['k1'] = 'v1'
    print(dd['k1'], dd['k2'])
    # OrderedDict是一个可以保持key顺序的dict
    d = dict()
    d['a'] = 1
    d['b'] = 1
    d['c'] = 1
    d['d'] = 1
    d['e'] = 1
    print(d.keys(), type(d))
    od = OrderedDict([('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1)])
    print(od, type(od))
    # LastUpdatedOrderedDict
    luod = LastUpdatedOrderedDict(3)
    luod['a'] = 1
    luod['b'] = 1
    luod['c'] = 1
    print(luod)
    luod['d'] = 1
    print(luod)
    # Counter是一个简单的计数器，实际上也是dict的一个子类
    c = Counter()
    for ch in 'programming':
        c[ch] = c[ch] + 1
    print(c)
