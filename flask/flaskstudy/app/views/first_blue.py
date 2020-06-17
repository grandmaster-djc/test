#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/5/28 11:06
# @Author  : djc
# @File    : first_blue.py
from flask import Blueprint, render_template

blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    return render_template('first_model.html')

