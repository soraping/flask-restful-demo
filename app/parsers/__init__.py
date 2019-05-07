#!/usr/bin/env python3
# encoding: utf-8

"""

@author: caoshiping
@contact: soraping@163.com
@file: __init__.py.py
@time: 2019-01-15 15:02
@desc:

"""

__author__ = ['"caoshiping":<soraping@163.com>']

from flask_restful import reqparse

# 基础请求参数
base_parsers = reqparse.RequestParser()
base_parsers.add_argument('User-Agent', type=str, location='headers')

# 列表基础请求参数
base_list_parsers = base_parsers.copy()
base_list_parsers.add_argument('pageNum', type=int)
base_list_parsers.add_argument('pageSize', type=int)