#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/9 
# Author    : smart
# @File     : 递归.py
# @Software : PyCharm
def sum(n):
    if n == 1:
        return 1
    else:
        return n+sum(n-1)


print(sum(100))