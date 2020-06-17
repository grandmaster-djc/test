#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/6/5 15:28
# @Author  : djc
# @File    : ext.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)


