#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 10:01
# @Author  : xujun
# @Email   : xujunrt@163.com

import collections


def sort_by_value(d, reverse=False):
    """
    dict 按照 value 排序，默认按照升序排序
    :param d: 待排序的dict
    :param reverse: False 表示升序排序, True 表示降序排序
    :return: 返回一个有序的dict
    """
    sorted_list = sorted(d.items(), key=lambda item: item[1], reverse=reverse)
    ret_dict = collections.OrderedDict()
    for item in sorted_list:
        k, v = item
        ret_dict[k] = v
    return ret_dict


def get_top_k(d, k=1):
    """
    获取 dict 中的前 k 个元素
    :param d: 输入的 dict
    :param k: 需要获取的数量
    :return: d 的前 k 个元素组成的 dict
    """
    ret_dict = collections.OrderedDict()
    cnt = 0
    for key, value in d.items():
        if cnt < k:
            cnt += 1
            ret_dict[key] = value
        break
    return ret_dict
