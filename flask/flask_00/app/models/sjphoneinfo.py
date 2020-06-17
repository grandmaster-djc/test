#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/6/5 16:05
# @Author  : djc
# @File    : sjphoneinfo.py
from app.ext import db
from sqlalchemy.sql import func
from datetime import datetime


class PhoneInfo(db.Model):
    """
    手机租借信息库
    """
    __tablename__ = 'phone_info'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    phoneId = db.Column(db.SMALLINT, primary_key=True, nullable=False, comment='手机记录id')
    sys = db.Column(db.VARCHAR(32), nullable=False, comment='操作系统')
    phoneName = db.Column(db.VARCHAR(32), nullable=False, comment='设备名称/型号')
    treasureId = db.Column(db.VARCHAR(32), nullable=False, comment='资产编号')
    boughtTime = db.Column(db.DateTime, default=datetime.now, nullable=False, comment='机型购买时间')
    image = db.Column(db.String(128), comment='图片链接')
    user = db.Column(db.String(32), comment='借用人员')
    useTime = db.Column(db.DateTime, comment='借出日期')
    isReturn = db.Column(db.BOOLEAN(1), default=0, comment='是否归还, 0-已归还，1-未归还')
    returnTime = db.Column(db.DateTime, comment='归还日期')
    isAbandoned = db.Column(db.BOOLEAN(1), default=0, comment='是否已报废, 0-未报废，1-已报废')
    abandonedTime = db.Column(db.DateTime, comment='报废时间')
    operate = db.Column(db.String(32), comment='处理人员')
    isDeleted = db.Column(db.BOOLEAN(1), default=0, comment='是否已删除，0-未删除，1-已删除')
    CreateTime = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    DataChange_LastTime = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now(), comment='修改时间')




