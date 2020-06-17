#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/6/3 13:44
# @Author  : djc
# @File    : settings.py 设置
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE") or "sqlite"
    driver = dbinfo.get("DRIVER") or "sqlite"
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or ""
    port = dbinfo.get("PORT") or ""
    name = dbinfo.get("NAME") or ""
    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:
    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRECT_KEY = "djcssecrectkey"
    # Session, Cookies以及一些第三方扩展都会用到SECRET_KEY值

class DevelopConfig(Config):
    """
    开发环境
    """
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "zx123456!",
        "NAME": "reptileDB",
        "HOST": "cdb-hf4q669t.gz.tencentcdb.com",
        "PORT": "10018"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class TestConfig(Config):
    """
    测试环境
    """
    TESTING = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "zx123456!",
        "NAME": "reptileDB",
        "HOST": "cdb-hf4q669t.gz.tencentcdb.com",
        "PORT": "10018"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagingConfig(Config):
    """
    堡垒环境
    """
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "zx123456!",
        "NAME": "reptileDB",
        "HOST": "cdb-hf4q669t.gz.tencentcdb.com",
        "PORT": "10018"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):
    """
    生产环境
    """
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "zx123456!",
        "NAME": "reptileDB",
        "HOST": "cdb-hf4q669t.gz.tencentcdb.com",
        "PORT": "10018"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    "development": DevelopConfig,
    "testing": TestConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}
