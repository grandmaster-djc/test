#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/5/27 19:53
# @Author  : djc
# @File    : models.py 模型
from app.ext import db


class User(db.Model):
    """
    user表
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16))
    idcard = db.Column(db.String(32))
    phone = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()


class City(db.Model):
    __tablename__='city'
    cityid = db.Column(db.Integer, primary_key=True)
    cityname = db.Column(db.String(16))

    def save(self):
        db.session.add(self)
        db.session.commit()