import json
import logging
import unittest,requests
from lib.read_excel import *
from lib.db import *
from lib.case_log import log_case_info


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        cls.li=read_excel().excel_to_list(data_file,'test_user_rege')
    def test_reg_ok(self):
        case_date=read_excel().get_test_data(self.li,'reg_ok')
        # list = read_excel().excel_to_list('test_user_data.xlsx','test_user_reg')
        # r= read_excel().get_test_data(list,'reg_ok')
        # print(r['url'])
        # print(json.dumps(r['args']))
        # self.assertEqual(True, False)
        print(case_date)
        url = case_date.get('url')
        args=case_date.get('ares')
        expect_res=case_date.get('expect_res')
        print(args)
        a=json.loads(args).get("userName")

        print(check_user(a))
        if check_user(name=a):
            del_user(a)
        res=requests.post(url=url,json=json.loads(args))
        log_case_info('test_reg_ok',url,args,expect_res,res.text)
        # logging.info('测试用例：{}'.format('test_reg_ok'))
        # logging.info('url:{}'.format(url))
        # logging.info('请求参数：{}'.format(args))
        # logging.info('期望结果:{}'.format(expect_res))
        # logging.info('实际结果：{}'.format(res.text))
        self.assertIn(expect_res,res.text)
        del_user(a)
    def test_reg_err(self):
        case_date = read_excel().get_test_data(self.li, 'reg_err')
        url = case_date.get('url')
        args = case_date.get('ares')
        expect_res = case_date.get('expect_res')
        res = requests.post(url=url, json=json.loads(args))
        log_case_info('test_reg_err', url, args, expect_res, res.text)
        # logging.info('测试用例：{}'.format('test_reg_err'))
        # logging.info('url:{}'.format(url))
        # logging.info('请求参数：{}'.format(args))
        # logging.info('期望结果:{}'.format(expect_res))
        # logging.info('实际结果：{}'.format(res.text))
        self.assertIn(expect_res, res.text)
if __name__ == '__main__':
    unittest.main()
