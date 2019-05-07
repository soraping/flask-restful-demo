#!/usr/bin/env python3
# encoding: utf-8

"""

@author: caoshiping
@contact: soraping@163.com
@file: wx_user_token.models.py
@time: 2019-01-14 15:12
@desc:

"""

__author__ = ['"caoshiping":<soraping@163.com>']

from app.extensions import db


class WxVersionModel(db.Model):

    __tablename__ = 'wx_app_version_config'

    app_id = db.Column(db.String(100), db.ForeignKey("wx_user_token.app_id"), primary_key=True)
    online_version_num = db.Column(db.String(100))
    version_audit_num = db.Column(db.String(100))
    version_audit_id = db.Column(db.String(100))
    version_audit_status = db.Column(db.String(100))
    create_time = db.Column(db.DateTime)
    modify_time = db.Column(db.DateTime)

    @classmethod
    def get_version_audit_id(cls, app_id):
        return cls.query.filter_by(app_id=app_id).first().version_audit_id


class WxUserModel(db.Model):

    __tablename__ = 'wx_user_token'

    app_id = db.Column(db.String(100), unique=True, primary_key=True)
    owner = db.Column(db.String(100))
    access_token = db.Column(db.String(200))
    refresh_token = db.Column(db.String(200))
    ticket_expire_time = db.Column(db.DateTime)
    create_time = db.Column(db.DateTime)
    modify_time = db.Column(db.DateTime)
    auth_type = db.Column(db.String)
    scene = db.Column(db.String)
    version = db.relationship('WxVersionModel', backref='wx_user_token')

    def __repr__(self):
        return '<AdminId {}>'.format(self.owner)

    @classmethod
    def get_list(cls, args):

        query = cls.query

        app_id = args.get("app_id")
        owner = args.get("owner")
        auth_type = args.get("auth_type")
        scene = args.get("scene")

        if app_id is not None:
            query = query.filter_by(app_id=app_id)
        if owner is not None:
            query = query.filter_by(owner=owner)
        if auth_type is not None:
            query = query.filter_by(auth_type=auth_type)
        if scene is not None:
            query = query.filter_by(scene=scene)

        return query\
            .order_by(cls.create_time.desc())\
            .paginate(args['pageNum'], per_page=args['pageSize'], error_out=False)

    @classmethod
    def get_access_token(cls, app_id):
        return cls.query.filter_by(app_id=app_id).first().access_token