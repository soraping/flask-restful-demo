#!/usr/bin/env python3
# encoding: utf-8

"""

@author: caoshiping
@contact: soraping@163.com
@file: wxa_fields.py
@time: 2019-01-17 15:36
@desc:

"""

__author__ = ['"caoshiping":<soraping@163.com>']

from flask_restful import fields
from app.fields import base_success_fields


wxa_bind_tester = base_success_fields({
    "errcode": fields.String,
    "errmsg": fields.String,
    "userstr": fields.String
})

wxa_version_fields = base_success_fields({
    "errcode": fields.String,
    "errmsg": fields.String
})