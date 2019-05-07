#!/usr/bin/env python3
# encoding: utf-8

"""

@author: caoshiping
@contact: soraping@163.com
@file: wxa_parser.py
@time: 2019-01-17 15:30
@desc:

"""

__author__ = ['"caoshiping":<soraping@163.com>']

from app.parsers import base_parsers

"""体验二维码"""
wxa_qrcode_parser = base_parsers.copy()
wxa_qrcode_parser.add_argument('path', type=str, required=True, help="path is required")
# 展示路径
wxa_qrcode_parser.add_argument('app_id', type=str, required=True, help="app_id is required")


"""绑定体验用户"""
wxa_bind_tester_parser = base_parsers.copy()
# 个人微信号
wxa_bind_tester_parser.add_argument('wechatid', type=str, required=True, help="wechatid is required")
wxa_bind_tester_parser.add_argument('app_id', type=str, required=True, help="app_id is required")


"""小程序版本相关请求"""
wxa_version_parser = base_parsers.copy()
wxa_version_parser.add_argument('app_id', type=str, required=True, help="app_id is required")

"""小程序审核撤回"""
wxa_version_undo_code_audit = wxa_version_parser.copy()