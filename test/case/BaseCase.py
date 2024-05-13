# ��������


import unittest,requests,json,sys
import ast# �ַ���ת�ֵ�
from config.config import *
from lib.read_excel import *
from lib.case_log import log_case_info
sys.path.append('../..')# ͳһ����������·����������Ŀ·����
class BaceCase(unittest.TestCase):
    r = read_excel()
    @classmethod
    def setUpClass(cls):
        if cls.__name__ !='BaseCase':

            cls.data_list=cls.r.excel_to_list(data_file,cls.__name__)
    def get_case_data(self,case_name):
        return self.r.get_test_data(self.data_list,case_name)
    def send_request(self,case_data):
        case_name=case_data.get('case_name')
        url = case_data.get('url')
        args = case_data.get('ares')
        print(args)
        headers = case_data.get('headers')
        method = case_data.get('method')
        expect_res = case_data.get('expect_res')
        data_type = case_data.get('data_type')
        # get����
        if method.upper() == 'GET':
            res=requests.get(url=url,json=json.loads(args))
        #     ����ʽ����
        elif data_type.upper() == 'FORM':
            print(args)
            print(type(args))
#           res=requests.post(url=url,data=json.loads(args),headers=json.loads(headers))
            res=requests.post(url=url,data=args,headers=headers)
            log_case_info(case_name,url,args,expect_res,res.text)
        elif data_type.upper() == "JSON":# JSON��ʽ����
            args=json.loads(args)
            print(args)
            print(type(json.dumps(args)))
            res = requests.post(url=url,json=args)
            log_case_info(case_name, url, args, expect_res, res.json())
            # self.assertDictEqual(res.json(),ast.literal_eval(expect_res))
            self.assertIn(expect_res,res.text)
