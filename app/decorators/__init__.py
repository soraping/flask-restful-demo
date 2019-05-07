#!/usr/bin/env python3
# encoding: utf-8

"""

@author: caoshiping
@contact: soraping@163.com
@file: __init__.py.py
@time: 2019-01-15 19:39
@desc:

"""

__author__ = ['"caoshiping":<soraping@163.com>']

from functools import wraps


def responseData(func):
    """
    返回值封装
    :param:
    :return:
    """
    @wraps(func)
    def wrapper(*args):
        data = func(*args)
        result = {
            "data": data,
            "result": "ok",
            "message": "操作成功"
        }
        return result
    return wrapper


def responseList(func):
    """
    列表返回
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args):
        data = func(*args)
        result = {
            "data": {
                "dataList": data.items,
                "pageNum": data.page,
                "pageSize": data.per_page,
                "total": data.total
            },
            "result": "ok",
            "message": "操作成功"
        }
        return result
    return wrapper