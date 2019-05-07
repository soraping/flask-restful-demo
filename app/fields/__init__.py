#!/usr/bin/env python3
# encoding: utf-8

"""

@author: caoshiping
@contact: soraping@163.com
@file: __init__.py.py
@time: 2019-01-10 18:00
@desc:

"""

__author__ = ['"caoshiping":<soraping@163.com>']

from flask_restful import fields


def base_success_fields(result_fields):
    """
    成功返回
    :param result_fields:
    :return:
    """
    success_fields = {}
    success_fields['result'] = fields.String(default="ok")
    success_fields['data'] = fields.Nested(result_fields)
    success_fields['message'] = fields.String(default="操作成功")

    return success_fields


def base_list_fields(list_fields):
    """
    列表返回
    :param list_fields:
    :return:
    """
    data_list = {}
    data_list["dataList"] = fields.List(fields.Nested(list_fields))
    data_list["total"] = fields.Integer(default=0)
    data_list['pageNum'] = fields.Integer(default=0)
    data_list['pageSize'] = fields.Integer(default=0)
    return data_list
#
#
# def base_failed_fields(err_fields):
#     """
#     失败返回
#     :param err_fields:
#     :return:
#     """
#     err = {}
#     err["result"] = fields.String(default="failed")
#     err["message"] = fields.String(default="系统异常")