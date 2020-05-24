#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 10:24
# @Author  : xujun
# @Email   : xujunrt@163.com

import platform


def get_system():
    sysstr = platform.system()
    if sysstr == "Windows":
        return "windows"
    elif sysstr == "Linux":
        return "linux"
    else:
        return "others"
