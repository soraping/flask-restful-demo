#!/usr/bin/env python3
# encoding: utf-8

"""

@author: caoshiping
@contact: soraping@163.com
@file: wxa_url.py
@time: 2019-01-17 15:48
@desc:

"""

__author__ = ['"caoshiping":<soraping@163.com>']

# 生成体验二维码
WXA_QRCODE = 'https://api.weixin.qq.com/wxa/get_qrcode?access_token={}&path={}'
# 添加体验者
WXA_BIND_TESTER = 'https://api.weixin.qq.com/wxa/bind_tester?access_token={}'

# 为授权的小程序上传代码
WXA_VERSION_COMMIT = 'https://api.weixin.qq.com/wxa/commit?access_token={}'
# 小程序提交审核
WXA_VERSION_SUBMIT_AUDIT = 'https://api.weixin.qq.com/wxa/submit_audit?access_token={}'
# 查询某个指定版本的审核状态
WXA_VERSION_AUDIT_STATUS = 'https://api.weixin.qq.com/wxa/get_auditstatus?access_token={}'
# 小程序审核撤回
WXA_VERSION_UNDO_CODE_AUDIT = 'https://api.weixin.qq.com/wxa/undocodeaudit?access_token={}'
# 发布已通过审核的小程序
WXA_VERSION_RELEASE = 'https://api.weixin.qq.com/wxa/release?access_token={}'
# 小程序版本回退
WXA_VERSION_REVERT_CODE_RELEASE = 'https://api.weixin.qq.com/wxa/revertcoderelease?access_token={}'
