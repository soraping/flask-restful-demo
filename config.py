#!/usr/bin/env python3
# encoding: utf-8

"""

@author: caoshiping
@contact: soraping@163.com
@file: config.py
@time: 2019-01-10 15:06
@desc:

"""

__author__ = ['"caoshiping":<soraping@163.com>']


class Config(object):

    DEBUG = True
    PORT = 5000
    HOST = "0.0.0.0"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "SOME SECRET"

    @staticmethod
    def init_app(self):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


class Test1Config(Config):
    SQLALCHEMY_DATABASE_URI = ""


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ""


config = {
        'development': DevelopmentConfig,
        'test1': Test1Config,
        'production': ProductionConfig,
        'default': DevelopmentConfig
}