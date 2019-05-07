#!/usr/bin/env python3
# encoding: utf-8

"""

@author: caoshiping
@contact: soraping@163.com
@file: wx_user_api.py
@time: 2019-01-14 11:15
@desc: 微信授权用户信息

"""

__author__ = ['"caoshiping":<soraping@163.com>']

from flask_restful import Resource, marshal_with
from app.apis import api
from app.decorators import responseList
from app.models import wx_user_models
from app.parsers import wx_user_parser
from app.fields import wx_user_fields


class WxUserListResource(Resource):
    """
    用户列表小程序公众号列表信息查询
    /api/wx_user_token?pageNum=0&&pageSize=2&&scene=o2o&&app_id=wx7ec0e4f7a198dac6
    """
    @marshal_with(wx_user_fields.wx_user_list_fields)
    @responseList
    def get(self):
        args = wx_user_parser.wx_user_list_parser.parse_args()
        return wx_user_models.WxUserModel.get_list(args)


api.add_resource(WxUserListResource, '/wx_user_list', endpoint='wx_user_list')
