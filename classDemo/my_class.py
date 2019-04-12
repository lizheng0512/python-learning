#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2019/4/9 11:40
"""

__author__ = 'liz'


class Animal(object):
    def run(self):
        print('animal running...')


class Pet(object):
    def run(self):
        print('pet running..')

    def eat(self, food='meat'):
        print('pet eating %s' % food)


class MyDog(Animal, Pet):

    def eat(self, food='meat'):
        super(MyDog, self).eat('fruit')

    # 规定MyDog只允许有name和age两个属性, 但是只影响当前类的实例, 子类的实例不受影响
    # __slots__ = ('name', 'age')

    # 实现了__len__方法就可以被len()调用
    def __len__(self):
        return 1

    # 类似于java的toString()
    def __str__(self):
        return 'MyDog: [name: %s, age: %s, sex: %s]' % (self.name, self.age, self.sex)

    @property
    def sex(self):
        print('sex')
        return self._sex

    @sex.setter
    def sex(self, value):
        print('set sex.')
        if not isinstance(value, str):
            raise ValueError('sex must be str!')
        self._sex = value


class Fib(object):
    def __init__(self):
        # 初始化斐波那契数列前两个数
        self.a, self.b = 0, 1

    # 实现该方法将实例可以作为可迭代对象
    # 实例本身就是一个迭代对象, 返回self
    def __iter__(self):
        return self

    # for循环会不断调用该方法
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration
        return self.a

    # 实现该方法可以将实例像list按下标取出元素一样进行操作
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 0, 1
            for i in range(item):
                a, b = b, a + b
            return a
        elif isinstance(item, slice):
            # 当传入的是切片时
            start = item.start
            stop = item.stop
            if start is None:
                print('start is none')
                start = 0
            a, b = 1, 1
            result = []
            for x in range(stop):
                if x >= start:
                    result.append(a)
                a, b = b, a + b
            return result

    # 实现该方法可以通过实例调用不存在的属性而不报错
    def __getattr__(self, item):
        pass

    def __call__(self, *args, **kwargs):
        args.index()


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, item))

    # 实现该方法可以让实例被调用
    def __call__(self, *args, **kv):
        # s = str(self._path)
        # s = s[:s.rindex('/')]
        # return Chain('%s/%s' % (s, fix))
        return Chain('%s/%s' % (self._path, args[0]))

    def __str__(self):
        return self._path


if __name__ == '__main__':
    print('Hello world!')
    dog = MyDog()
    dog.name = 'lex'
    dog.age = 123
    dog.sex = '1'
    print(dog)
    dog.run()
    dog.eat()

    animal = Animal()
    animal.run()

    # fib = Fib()
    # for n in fib:
    #     print(n)

    # print(fib[6])
    # print(fib[:3])
    #
    # print(fib.a1)

    print(Chain().abc.qwe.users('zhangsan').qqq)
