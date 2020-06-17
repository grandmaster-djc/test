#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/5/27 19:52
# @Author  : djc
# @File    : __init__.py.py
from flask import Flask
from app.ext import init_ext
from app.views import init_views
from app.settings import envs


def create_app(env):
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zx123456!@cdb-hf4q669t.gz.tencentcdb.com:10018/' \
    #                                         'reptileDB'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # # 设置这一项是每次请求结束后不会自动提交数据库中的变动

    app.config.from_object(envs.get(env))  # 加载配置，运行环境
    init_ext(app)

    init_views(app=app)
    return app