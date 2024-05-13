#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/26 
# Author    : smart
# @File     : case_log.py
# @Software : PyCharm
# 封装日志
from config import *

import logging
import json
def log_case_info(case_name,url,args,expect_res,res_text):
    if isinstance(args,dict):
        args = json.dumps(args,ensure_ascii=False)
        logging.info('测试用例：{}'.format(case_name))
        logging.info('url:{}'.format(url))
        logging.info('请求参数：{}'.format(args))
        logging.info('期望结果:{}'.format(expect_res))
        logging.info('实际结果：{}'.format(res_text))