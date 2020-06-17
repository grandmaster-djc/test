#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/6/3 13:44
# @Author  : djc
# @File    : ext.py 第三方扩展
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # 数据库迁移




db = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
        db.init_app(app=app)
        migrate.init_app(app, db)