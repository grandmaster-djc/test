#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/5/28 11:12
# @Author  : djc
# @File    : second_blue.py
from flask import Blueprint

second = Blueprint('second', __name__)


@second.route('/1')
def second_0():
    # 函数名不能与蓝图变量名相同
    return '这是第二页'



