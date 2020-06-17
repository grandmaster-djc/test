#!/usr/bin/env python 
#-*-coding:utf-8-*-
# @Time    : 2020/6/11 15:04
# @Author  : djc
# @File    : createPhoneInfo.py


class CreatePhoneInfo(object):

    def create(self, data):
        try:
            data = request.get_data()
            json_data = json.loads(data)
            a = json_data["year"]
            b = json_data["asdad"]

        except KeyError as k:
            return "keyError: key值 %s 未找到" % k

        else:
            return json_data
if __name__ == '__main__':
    a = CreatePhoneInfo()
    a.create(2)


