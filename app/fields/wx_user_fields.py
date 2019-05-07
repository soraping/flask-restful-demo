#!/usr/bin/env python3
# encoding: utf-8

"""

@author: caoshiping
@contact: soraping@163.com
@file: wx_user_fields.py
@time: 2019-01-14 15:04
@desc:

"""

__author__ = ['"caoshiping":<soraping@163.com>']

from flask_restful import fields
from app.fields import base_success_fields, base_list_fields

wx_version = {
    # 线上启用版本
    'online_version_num': fields.String,
    # 提交测试版本
    'version_audit_num': fields.String,
    # 审核状态
    'version_audit_status': fields.String
}

wx_user_info = {
    'app_id': fields.String,
    'owner': fields.String,
    # 授权类型 MP MP_APP
    'auth_type': fields.String,
    # 场景
    'scene': fields.String,
    'create_time': fields.DateTime,
    'modify_time': fields.DateTime,
    # 版本信息
    'version': fields.Nested(wx_version)
}

wx_user_info_fields = base_success_fields(wx_user_info)

wx_user_list_fields = base_success_fields(base_list_fields(wx_user_info))