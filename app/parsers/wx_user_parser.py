#!/usr/bin/env python3
# encoding: utf-8

"""

@author: caoshiping
@contact: soraping@163.com
@file: wx_user_parser.py
@time: 2019-01-15 15:03
@desc:

"""

__author__ = ['"caoshiping":<soraping@163.com>']

from app.parsers import base_parsers, base_list_parsers

# 根据字段查询单个用户信息
wx_user_filter_parser = base_parsers.copy()
wx_user_filter_parser.add_argument('app_id', type=str, required=True, help="app_id is required")


# 用户TOKEN列表查询
wx_user_list_parser = base_list_parsers.copy()
wx_user_list_parser.add_argument('app_id', type=str)
wx_user_list_parser.add_argument('owner', type=str)
wx_user_list_parser.add_argument('scene', type=str)
wx_user_list_parser.add_argument('auth_type', type=str)