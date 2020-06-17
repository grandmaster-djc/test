#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/6/3 14:05
# @Author  : djc
# @File    : db_operate.py 数据库相关操作
from flask import Blueprint
from app.models.models import db, User

db_operate = Blueprint('dboperate', __name__)


@db_operate.route('/create_db/')
def create_db():
    """
    创建user表
    :return:
    """
    db.create_all()
    return '创建成功'


@db_operate.route('/drop_db/')
def drop_db():
    db.drop_all()
    return "删除成功"


@db_operate.route('/add_user/')
def add_user():
    """
    增加用户信息
    :return:
    """
    user = User()
    user.username = "tom"
    user.save()
    # db.session.add(user)
    # db.session.commit()
    return "添加成功"






