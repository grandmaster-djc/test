#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/6/11 17:04
# @Author  : djc
# @File    : test.py

try:
    # 异常捕获块，把可能出错的代码放这
    print(1/0)

except Exception as e:  # 异常处理块
    print('%s 错误' % e)

print(2222)













