#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2019/4/12 16:54
"""

__author__ = 'liz'

import os

if __name__ == '__main__':
    # 列出当前目录的绝对路径
    abspath = os.path.abspath(".")
    print(abspath)
    # 要在某个目录下新建一个目录, 返回新目录完整路径
    join = os.path.join(abspath, 'test_dir')
    print(join)
    # 创建目录
    os.mkdir(join)
