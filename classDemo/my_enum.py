#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2019/4/9 16:13
"""

__author__ = 'liz'

from enum import Enum, unique

Month = Enum('month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


@unique
class WeekDay(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


if __name__ == '__main__':
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

    for name, member in WeekDay.__members__.items():
        print(name, '=>', member, ',', member.value)
