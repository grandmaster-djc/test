#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/5/28 11:06
# @Author  : djc
# @File    : first_blue.py
from flask import Blueprint, render_template, redirect, url_for, request

blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    return render_template('first_model.html')


@blue.route('/index/get_int_id/<int:id>/')
@blue.route('/index/get_string_id/<string:id>/')
def get_id(id):
    print(id)
    print(type(id))
    return 'success'


@blue.route('/index/get_any/<any(a,b,c):an>/')
def get_any(an):
    print(an)
    print(type(an))
    return 'success'


@blue.route('/index/redirect/')
def red():
    return redirect(url_for('blue.get_any', an='a'))


@blue.route('/index/request/', methods=['GET', 'POST', 'PUT'])
def get_request():
    if request.method == 'GET':
        return 'get success %s' % request.remote_addr
    elif request.method == 'POST':
        return 'post success %s' % request.remote_addr
    else:
        return '%s not support' % request.method
