#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/6/5 16:13
# @Author  : djc
# @File    : sjphone_info.py
# 手机资产设备相关操作，涉及表phone_info，phone_info_log
from flask import Blueprint, jsonify , request
from app.models.sjphoneinfo import db, PhoneInfo
import json
#from app.service.createPhoneInfo import CreatePhoneInfo


db_phone_info = Blueprint('phone_info', __name__)


# @db_phone_info.route('/create_phone_info/')
# def create_phone_info():
#     """
#     创建user表
#     :return:
#     """
#     db.create_all()
#     return '创建成功'
#
#
# @db_phone_info.route('/drop_phone_info/')
# def drop_phone_info():
#     db.drop_all()
#     return "删除成功"


@db_phone_info.route('/create_info/', methods=['GET', 'POST', 'PUT'])
def create_info():
    if request.method.upper() == 'POST':
        try:
            data = request.get_data()
            json_data = json.loads(data)

        except ValueError as v:
            return "ValueError: %s ，请检验传参" % v

        except KeyError as k:
            return "keyError: key值 %s 未找到" % k

        else:
            return json_data
    else:
        return '%s not support' % request.method



