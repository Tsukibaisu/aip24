#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/15 
# Author    : smart
# @File     : 请求get.py
# @Software : PyCharm
import requests

url='http://www.baidu.com/'
ss={
    "kw":'抖音网页版'
}
req = requests.get(url,ss)

print(req.text)

req.encoding='utf-8'


print(req.status_code)
print(req.url)
print(req.headers)
print(req.cookies)
print(req.text)
print(req.content)
