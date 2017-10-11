# coding=utf-8
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from selenium import webdriver

from Case.User.Data import Data
from .update import UsernameAndPassword


class Test004_RegisterError(unittest.TestCase):
    def setUp(self):
        u = Data
        self.driver = webdriver.Firefox()
        self.driver.get(u.register_url)
        time.sleep(3)
        # self.driver.maximize_window()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_registererror1(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.inputr("1", u.email, u.name, u.password, u.password)
        time.sleep(10)
        # 手动输入验证码
        uap.confirm()
        time.sleep(3)
        self.assertEqual(uap.errormsg(), "注册：企业不存在")

    def test_registererror2(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.inputr(u.businesscode, u.username, u.name, u.password, u.password)
        time.sleep(10)
        # 手动输入验证码
        uap.confirm()
        time.sleep(3)
        self.assertEqual(uap.errormsg(), "注册：数据库中已存在该记录")

    def test_registererror3(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.inputr(u.businesscode, u.email, u.name, u.password, u.password, "aaaaa")
        uap.confirm()
        time.sleep(3)
        self.assertEqual(uap.errormsg(), "注册：验证码不正确")

    def test_registererror4(self):
        uap = UsernameAndPassword(self.driver)
        uap.confirm()
        time.sleep(1)
        self.assertEqual(uap.popmsg(), "不能为空哦")

    def test_registererror5(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.inputr(u.businesscode, "1", u.name, u.password, u.password, "aaaaa")
        uap.confirm()
        time.sleep(1)
        self.assertEqual(uap.popmsg(), "请输入有效的电子邮件")

    def test_registererror6(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.inputr(u.businesscode, u.email, u.name, "1", "1", "aaaaa")
        uap.confirm()
        time.sleep(1)
        self.assertEqual(uap.popmsg(), "最少 6 个字")

    def test_registererror7(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.inputr(u.businesscode, u.email, u.name, u.password, "1234567", "aaaaa")
        uap.confirm()
        time.sleep(1)
        self.assertEqual(uap.popmsg(), "你的输入不相同")

    # def test_registerrror8(self):
    #     u = Data
    #     uap = UsernameAndPassword(self.driver)
    #     uap.inputr(u.businesscode, u.email, u.name, u.password, u.password, "aaaaa")
    #     time.sleep(1)
    #     uap.confirm()
    #     uap.confirm()
    #     time.sleep(3)
    #     self.assertEqual(uap.errormsg(), "注册：验证码已失效")

    def test_loginerror9(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.inputr(u.businesscode_only, u.email, u.name, u.password, u.password)
        time.sleep(10)
        # 手动输入验证码
        uap.confirm()
        time.sleep(3)
        self.assertEqual(uap.errormsg(), "注册：用户数超出限制")


if __name__ == "Test004_registererror":
    # unittest.main()
    suite = unittest.TestSuite
    suite.addTest(Test004_registererror, "test_registererror1")
    suite.addTest(Test004_registererror, "test_registererror2")
    suite.addTest(Test004_registererror, "test_registererror3")
    suite.addTest(Test004_registererror, "test_registererror4")
    suite.addTest(Test004_registererror, "test_registererror5")
    suite.addTest(Test004_registererror, "test_registererror6")
    suite.addTest(Test004_registererror, "test_registererror7")
    # suite.addTest(Test004_registererror, "test_registererror8")
    suite.addTest(Test004_registererror, "test_registererror9")
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = "D:/搜狗高速下载/Python-master/Case/result.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(fp, "测试报告", "用例执行情况：")
    runner.run(suite)
    fp.close()