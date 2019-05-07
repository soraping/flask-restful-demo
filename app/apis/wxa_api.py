#!/usr/bin/env python3
# encoding: utf-8

"""

@author: caoshiping
@contact: soraping@163.com
@file: wxa_api.py
@time: 2019-01-17 15:16
@desc:  小程序

"""

__author__ = ['"caoshiping":<soraping@163.com>']

import requests
import json
import base64
from flask_restful import Resource, marshal_with
from app.parsers import wxa_parser
from app.apis import api
from app.models import wx_user_models
from app.fields import wxa_fields
from app.decorators import responseData
from app.wxa_url import WXA_BIND_TESTER, WXA_QRCODE, WXA_VERSION_UNDO_CODE_AUDIT


class WxaQrcodeResource(Resource):
    """
    获取小程序体验码
    """
    @responseData
    def get(self):
        args = wxa_parser.wxa_qrcode_parser.parse_args()
        # 获取令牌
        access_token = wx_user_models.WxUserModel.get_access_token(args.get("app_id"))
        # 调用微信接口
        result = requests.get(WXA_QRCODE.format(access_token, args.get('path')))
        if result.ok is True:
            return base64.b64encode(bytes(result.text, encoding='utf-8')).decode()
        else:
            return json.loads(result.text)

        # resp = make_response(result.text)
        # resp.headers["Content-Type"] = 'image/jpeg'
        # resp.headers["Content-disposition"] = "attachment; filename='QRCode.jpg'"
        # return resp


class WxaBindTester(Resource):
    """
    添加用户为体验者
    """
    @marshal_with(wxa_fields.wxa_bind_tester)
    @responseData
    def post(self):
        form = wxa_parser.wxa_bind_tester_parser.parse_args()
        app_id = form.get("app_id")
        # 获取令牌
        access_token = wx_user_models.WxUserModel.get_access_token(app_id)
        # 调用微信接口绑定用户
        payload = json.dumps({"wechatid": form.get("wechatid")})
        result = requests.post(WXA_BIND_TESTER.format(access_token), data=payload)
        return json.loads(result.text)


class WxaUndoCodeAudit(Resource):
    """
    小程序撤回审核
    """
    @marshal_with(wxa_fields.wxa_version_fields)
    @responseData
    def get(self):
        args = wxa_parser.wxa_version_undo_code_audit.parse_args()
        access_token = wx_user_models.WxUserModel.get_access_token(args.get('app_id'))
        result = requests.get(WXA_VERSION_UNDO_CODE_AUDIT.format(access_token))
        return result.text


api.add_resource(WxaQrcodeResource, '/wxa/qrcode', endpoint='wxa_qrcode')
api.add_resource(WxaBindTester, '/wxa/bind_tester', endpoint='wxa_bind_tester')
api.add_resource(WxaUndoCodeAudit, '/wxa/undocodeaudit', endpoint='wx_undo_code_audit')