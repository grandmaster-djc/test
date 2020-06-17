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

    def save(self):
        db.session.add(self)
        db.session.commit()


class Address(db.Model):
    __tablename__='address'
    id = db.Column(db.Integer, primary_key=True)
    addressname = db.Column(db.String(16))

    def save(self):
        db.session.add(self)
        db.session.commit()