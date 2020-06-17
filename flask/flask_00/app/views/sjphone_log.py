#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/6/11 14:53
# @Author  : djc
# @File    : sjphone_log.py
from flask import Blueprint
from app.models.sjphonelog import db, PhoneInfolog

db_phone_infologs = Blueprint('phone_infologs', __name__)


@db_phone_infologs.route('/create_phone_infologs/')
def create_phone_infologs():
    """
    创建user表
    :return:
    """
    db.create_all()
    return '创建成功'


@db_phone_infologs.route('/drop_phone_infologs/')
def drop_phone_infologs():
    db.drop_all()
    return "删除成功"