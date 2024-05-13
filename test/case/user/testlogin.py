import unittest
from lib import xzs_login


class MyTestCase(unittest.TestCase):
    xzs=xzs_login.login()
    def test_login_01(self):
        t=self.xzs.login("student1", "123456")
        self.assertIn("成功",t.text)
    def test_login_02(self):
        t=self.xzs.login("student", "")
        self.assertIn("用户名或密码错误",t.text)

if __name__ == '__main__':
    unittest.main()
