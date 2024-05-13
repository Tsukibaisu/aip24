#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/7 
# Author    : smart
# @File     : test_suit.py
# @Software : PyCharm
import unittest,sys
sys.path.append('../..')
from test.case.user.test_user_login import test_user_login
from test.case.user.test_user_reg import test_user_rege

smoke_suit=unittest.TestSuite()
smoke_suit.addTests([test_user_login('test_login_success'),test_user_rege('test_user_reg')])

def get_suit(suit_name):
    suit_name = unittest.TestSuite()
    suit_name.addTests([test_user_login('test_login_success'),test_user_rege('test_user_reg')])

    return suit_name
unittest.TextTestRunner(verbosity=2).run(smoke_suit)

