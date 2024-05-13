import unittest,requests
from lib.db1p2p import  *



class MyTestCase(unittest.TestCase):
    url='http://192.168.55.13:8080/p2p_management/addProduct'
    def test_p2p_ok(self):
        # 如果有0005
        if check_p2p('0005'):
            # 直接删除0005
            del_p2p('0005')

        data={"proNum":"0005","proName":"小米椒","proLimit":"2","annualized":"41"}

        r=requests.post(url=self.url,json=data)

        self.assertNotIn('失败',r.text)

        self.assertTrue(check_p2p('0005'))
        del_p2p('0005')

    def test_p2p_err(self):

        data = {"proNum":"0005","proName":"小米椒","proLimit":"2","annualized":"41%"}

        r = requests.post(url=self.url, json=data)

        self.assertIn('400',r.text)



if __name__ == '__main__':
    unittest.main()
