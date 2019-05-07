#!/usr/bin/env python3
# encoding: utf-8

"""

@author: caoshiping
@contact: soraping@163.com
@file: __init__.py.py
@time: 2019-01-10 11:31
@desc:

"""

__author__ = ['"caoshiping":<soraping@163.com>']

from flask import Flask
from config import config
from app.apis import api_blueprint
from app.extensions import db


def create_app(config_filename):

    app = Flask(__name__)
    app.config.from_object(config[config_filename])
    config[config_filename].init_app(app)
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    app.register_blueprint(api_blueprint)