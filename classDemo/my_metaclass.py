#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
基于metaclass实现简单ORM
Created on 2019/4/9 16:51
"""

__author__ = 'liz'


# 定义字段的基类, 放置字段名和字段类型
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.name, self.column_type)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 定义元类, 用于绑定字段映射和表名
class ModelMetaClass(type):
    # 元类的__new__方法参数依次为: 当前准备创建的类的对象, 类的名字, 类继承的父类的集合, 类的方法和属性集合
    def __new__(cls, name, bases, attrs):
        # 如果创建的是Model类, 则不处理
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        # 用于存储类属性和字段映射
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping %s => %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        # 放置到类的属性中
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


# 定义实体的直接基类Model
class Model(dict, metaclass=ModelMetaClass):
    # Model继承自dict
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    # 通过user.name的方式获取属性时
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % item)

    # user.name = '张三'的方式设置属性的时候, 存入dict
    def __setattr__(self, key, value):
        print('__setattr__')
        self[key] = value

    # 定义保存方法, 通过元类设置的__mappings__和__table__来获取属性和表名
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL:', sql)
        print('ARGS:', str(args))


class User(Model):
    id = IntegerField('id')
    name = StringField('name')
    age = IntegerField('age')

    def hello(self):
        print('hello')


if __name__ == '__main__':
    user = User(id=1, name='zhangsan', age=22, job='programmer')
    user.save()
