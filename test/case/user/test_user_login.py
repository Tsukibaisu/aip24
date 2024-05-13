#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/6 
# Author    : smart
# @File     : test_user_login.py
# @Software : PyCharm
# 登录用用例基类来写
from test.case.BaseCase import BaceCase
class test_user_login(BaceCase):
    def test_login_success(self):
        """level1:正常登录"""
        case_data=self.get_case_data('login_ok')
        self.send_request(case_data)
    def test_login_daill(self):
        casr_data=self.get_case_data('login_err1')
        self.send_request(casr_data)

    def test_login_dail2(self):
        casr_data = self.get_case_data('login_err2')
        self.send_request(casr_data)
if __name__ == '__main__':
    test_user_login()