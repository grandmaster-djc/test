#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/5/26 15:08
# @Author  : djc
# @File    : helloflask.py
import os
from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app

env = os.environ.get("FLASK_ENV", "development")
app = create_app(env)
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()
