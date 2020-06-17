#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/6/5 15:24
# @Author  : djc
# @File    : run.py
import os
from App import create_app
from flask_script import Manager

env = os.environ.get("FLASK_ENV", "development")
# 系统环境变量
app = create_app(env)
manager = Manager(app=app)
manager.add_command('', )

if __name__ == '__main__':
    manager.run()






