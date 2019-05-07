#!/usr/bin/env python3
# encoding: utf-8

"""

@author: caoshiping
@contact: soraping@163.com
@file: app.py
@time: 2019-01-10 11:27
@desc:

"""

__author__ = ['"caoshiping":<soraping@163.com>']

from app import create_app

app = create_app('development')

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])