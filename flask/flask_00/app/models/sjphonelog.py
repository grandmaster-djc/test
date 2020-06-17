#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/6/11 14:53
# @Author  : djc
# @File    : sjphonelog.py
from app.ext import db
from sqlalchemy.sql import func


class PhoneInfolog(db.Model):
    """
    归还日志表
    """
    __tablename__ = 'phone_info_log'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    logId = db.Column(db.SMALLINT, primary_key=True, nullable=False, comment='日志id')
    user = db.Column(db.String(32), comment='借用人员')
    user_operate = db.Column(db.Enum('0', '1'), comment='借用操作，0-借出，1-归还')
    comment = db.Column(db.String(128), comment='描述')
    isDeleted = db.Column(db.BOOLEAN(1), default=0, comment='是否已删除，0-未删除，1-已删除')
    CreateTime = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    DataChange_LastTime = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now(), comment='修改时间')

