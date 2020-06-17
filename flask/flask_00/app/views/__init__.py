#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/5/27 19:53
# @Author  : djc
# @File    : views.py
from .first_blue import blue
from .second_blue import second
from .db_operate import db_operate
from .sjphone_info import db_phone_info
from .sjphone_log import db_phone_infologs


def init_views(app):
    """
    统一注册，方便管理
    :param app:
    :return:
    """
    app.register_blueprint(blue)
    app.register_blueprint(second)
    app.register_blueprint(db_operate)
    app.register_blueprint(db_phone_info)
    app.register_blueprint(db_phone_infologs)
