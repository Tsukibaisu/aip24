import json
import unittest,requests,ddt
from config import *
from lib import read_excel
from lib.case_log import log_case_info
import os,sys
from config.config import *
# from read_excel import *
# from db import *


# class MyTestCase(unittest.TestCase):

    # @classmethod
    # 自己写的
    # def setUpClass(cls) :
    #     cls.li=read_excel().excel_to_list('test_user_data.xlsx','test_user_login')
    # def test_login_ok(self):
    #     case_date=read_excel().get_test_data(self.li,'login_ok')
    #
    #     print(case_date)
    #     url = case_date.get('url')
    #     args=case_date.get('ares')
    #     expect_res=case_date.get('expect_res')
    #     print(args)
    #     a=json.loads(args).get("userName")
    #     data={"userName":"student1","password":"123456","remember":None}
    #     r = requests.post(url=url, json=data)
    #     result = {"code":1,"message":"成功","response":{"id":None,"userUuid":None,"userName":"student1","password":None,"realName":None,"age":None,"sex":None,"birthDay":None,"userLevel":None,"phone":None,"role":None,"status":None,"imagePath":None,"createTime":None,"modifyTime":None,"lastActiveTime":None,"deleted":None,"wxOpenId":None}}
    #     self.assertDictEqual(r.json(), result)
    #     print(expect_res)
    #     print(check_user(a))
    #
    #
    # def test_login_err1(self):
    #     case_date = read_excel().get_test_data(self.li, 'login_err1')
    #     url = case_date.get('url')
    #     args = case_date.get('ares')
    #     expect_res = case_date.get('expect_res')
    #     print(url)
    #     data = {"userName":"student","password":"123456","remember": None}
    #     r = requests.post(url=url, json=data)
    #     result = {"code":402,"message":"用户名或密码错误","response":None}
    #     self.assertDictEqual(r.json(), result)
    #     print(expect_res)
    #     print(args)
    # def test_login_err2(self):
    #     case_date = read_excel().get_test_data(self.li, 'login_err2')
    #     url = case_date.get('url')
    #     args = case_date.get('ares')
    #     expect_res = case_date.get('expect_res')
    #     print(url)
    #     data = {"userName":"","password":"123456","remember": None}
    #     r = requests.post(url=url, json=data)
    #     result = {"code":402,"message":"用户名或密码错误","response":None}
    #     self.assertDictEqual(r.json(), result)
    #     print(expect_res)
    #     print(args)
    #
    # def test_login_err3(self):
    #     case_date = read_excel().get_test_data(self.li, 'login_err3')
    #     url = case_date.get('url')
    #     args = case_date.get('ares')
    #     expect_res = case_date.get('expect_res')
    #     print(url)
    #     data = {"userName":"student1","password":"","remember": None}
    #     r = requests.post(url=url, json=data)
    #     result = {"code": 402, "message": "用户名或密码错误", "response": None}
    #     self.assertDictEqual(r.json(), result)
    #     print(expect_res)
    #     print(args)
#     老师写的
def read():
    r=read_excel.read_excel()
    l=r.excel_to_list(data_file,'test_user_login')
    t=[]
    for i in range(len(l)):
        t.append(l[i]['case_name'])
    return t
@ddt.ddt
class MyTestCase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) :
    #     # cls.li = read_excel().excel_to_list('test_user_data.xlsx', 'test_user_login')
    #     cls.r=read_excel.read_excel()
    #     cls.l=cls.r.excel_to_list('test_user_data.xlsx','test_user_login')
    @ddt.data(*read())
    def test_login(self,name):
        r=read_excel.read_excel()
        l=r.excel_to_list(data_file,'test_user_login')
        t=r.get_test_data(l,name)
        # t = self.r.get_test_data(self.l, name)
        url = t.get('url')
        args=t.get('ares')
        expect_res=t.get('expect_res')
        # 转换成字符串
        data=json.loads(args)
        # 发送post请求
        r = requests.post(url, json=data)
        log_case_info(name, url, args, expect_res, r.text)
        # logging.info('测试用例：{}'.format('name'))
        # logging.info('url:{}'.format(url))
        # logging.info('请求参数：{}'.format(args))
        # logging.info('期望结果:{}'.format(expect_res))
        # logging.info('实际结果：{}'.format(r.text))
        self.assertIn(expect_res,r.text)
if __name__ == '__main__':
    unittest.main()