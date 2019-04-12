#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2019/4/12 16:19
"""

__author__ = 'liz'

if __name__ == '__main__':
    # 利用with关键字打开文件, 可以不用手动调用close方法
    # r: 只读模式, rb 二进制只读模式, w 写模式
    with open("../hello_world.py", 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            print(line.strip("\n"))

    with open("test_file.txt", 'a') as f:
        lines = ['a\n', 'ab\n', 'abc\n']
        f.writelines(lines)


