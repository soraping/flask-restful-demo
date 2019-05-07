#!/usr/bin/env python3
# encoding: utf-8

"""

@author: caoshiping
@contact: soraping@163.com
@file: __init__.py.py
@time: 2019-01-10 18:04
@desc:

"""

__author__ = ['"caoshiping":<soraping@163.com>']

from flask import Blueprint
from flask_restful import Api

api_blueprint = Blueprint("apis", __name__, url_prefix='/api')
api = Api(api_blueprint, default_mediatype="application/json")

from . import wx_user_api
from . import wxa_api