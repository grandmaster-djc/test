#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/6/5 15:24
# @Author  : djc
# @File    : __init__.py.py
from flask import Flask
from App.configs.settings import envs
from App.ext import init_ext


def create_app(env):
    app = Flask(__name__)

    # 初始化项目配置
    app.config.from_object(envs.get(env))

    # 初始化扩展库 非路由相关
    init_ext(app)

    return app



