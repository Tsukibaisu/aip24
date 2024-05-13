import unittest
from test.case.user.testlogin import MyTestCase
from test_xzs_zuce import MyTestCase as m


class MyTestCase1(unittest.TestCase):
    def test_suit(self):
        # 创建一个suit
        suit=unittest.TestSuite()
        # 向suit中添加单个用例
        suit.addTest(MyTestCase('test_login_01'))
        # 向suit中添加多个用例
        suit.addTests([m('test_reg_ok'),m('test_reg_err')])
        # 生成文本格式测试报告
        with open("result.txt",'w') as f:
            unittest.TextTestRunner(stream=f,verbosity=2).run(suit)
    def test_makesuit(self):
        # makesuit将mytestcase中的所有yl添加到suit中
        suit1=unittest.makeSuite(MyTestCase)
        unittest.TextTestRunner(verbosity=2).run(suit1)
    def test_loader(self):
        # loader加载该测试类所有 用例并生成测试报告
        suit2=unittest.TestLoader().loadTestsFromTestCase(m)
        unittest.TextTestRunner(verbosity=2).run(suit2)
    # def test_discover(self):
    #     suit3=unittest.defaultTestLoader.discover('./')
    #     unittest.TextTestRunner(verbosity=2).run(suit3)

if __name__ == '__main__':
    unittest.main()
