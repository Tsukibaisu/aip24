#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/17 
# Author    : smart
# @File     : zhuc_login.py
# @Software : PyCharm
import requests
class login:
    def login(self,user,ps):
        url="http://127.0.0.1:8000/api/user/login"
        data={"userName":user,"password":ps,"remember":False}
        r= requests.post(url,json=data)
        return r
if __name__ == '__main__':
    l=login()
    print(l.login("student1", "123456").text)