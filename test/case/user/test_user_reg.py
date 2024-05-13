#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/6 
# Author    : smart
# @File     : test_user_reg.py
# @Software : PyCharm
from test.case.BaseCase import BaceCase
from lib.db import *
import json
class test_user_rege(BaceCase):
    def test_user_reg(self):
       '''注册用户'''
       case_data = self.get_case_data('reg_ok')
       print(case_data)
       userName = json.loads(case_data.get('ares')).get('userName')
       print(userName)
       if check_user(userName):
           del_user(userName)
       #      发送请求
       self.send_request(case_data)
       #  数据库断言
       self.assertTrue(check_user(userName))
       #  环境清理
       del_user(userName)
    def test_user_reg_exist(self):
        case_data = self.get_case_data('reg_err')

        userName = json.loads(case_data.get('ares')).get("userName")
        print(userName)
        if not check_user(userName):
            add_user(userName,'123456')
        self.send_request(case_data)
if __name__ == '__main__':
    test_user_rege()