#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2019/4/9 17:01
"""
import os

import numpy

__author__ = 'liz'


def similarity(multiple_feature, f):
    """余弦相似度计算, 支持批量计算
    Args:
        multiple_feature: 批量待比对矩阵: dim -> x*n, x特征值个数; n向量维度
        f: 1*n的向量, n向量维度
    Returns:
        余弦值结果向量: 1*x
    """
    x = multiple_feature.shape[0]
    multiple_norm = numpy.linalg.norm(multiple_feature, axis=1).reshape(x, 1)
    f_norm = numpy.linalg.norm(f, axis=1).reshape(1, 1)
    return multiple_feature.dot(f.T) / multiple_norm.dot(f_norm)


if __name__ == '__main__':
    print(os.name)
