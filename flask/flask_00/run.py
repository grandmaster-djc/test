#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/5/26 15:08
# @Author  : djc
# @File    : helloflask.py
import os
from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app

env = os.environ.get("FLASK_ENV", "development")  # 获取当前的flask环境变量
app = create_app(env)
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)  # 数据库迁移库


if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()
