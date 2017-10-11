# coding=utf-8
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from selenium import webdriver

from Case.User.Data import Data
from .update import UsernameAndPassword


class Test002_LoginError(unittest.TestCase):
    def setUp(self):
        u = Data
        self.driver = webdriver.Firefox()
        self.driver.get(u.url)
        time.sleep(5)
        # self.driver.maximize_window()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_loginerror1(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.input("1", u.password)
        time.sleep(10)
        # 手动输入验证码
        uap.confirm()
        time.sleep(3)
        self.assertEqual(uap.errormsg(), "登录：账号格式错误")

    def test_loginerror2(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.input(u.username, "1")
        time.sleep(10)
        # 手动输入验证码
        uap.confirm()
        time.sleep(3)
        self.assertEqual(uap.errormsg(), "登录：账号或密码不正确")

    def test_loginerror3(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.input(u.username, u.password, "aaaaa")
        uap.confirm()
        time.sleep(3)
        self.assertEqual(uap.errormsg(), "登录：验证码不正确")

    def test_loginerror4(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.input(u.username_deleted, u.password_deleted)
        time.sleep(10)
        # 手动输入验证码
        uap.confirm()
        time.sleep(3)
        self.assertEqual(uap.errormsg(), "登录：账号已被锁定,请联系管理员")

    def test_loginerror5(self):
        uap = UsernameAndPassword(self.driver)
        uap.confirm()
        time.sleep(1)
        self.assertEqual(uap.popmsg(), "不能为空哦")

    # def test_loginerror6(self):
    #     u = Data
    #     uap = UsernameAndPassword(self.driver)
    #     uap.input(u.username, u.password)
    #     time.sleep(300)
    #     uap.confirm()
    #     time.sleep(1)
    #     self.assertEqual(uap.errormsg(), "登录：验证码已失效")


if __name__ == "Test002_loginerror":
    # unittest.main()
    suite = unittest.TestSuite
    suite.addTest(Test002_LoginError, "test_loginerror1")
    suite.addTest(Test002_LoginError, "test_loginerror2")
    suite.addTest(Test002_LoginError, "test_loginerror3")
    suite.addTest(Test002_LoginError, "test_loginerror4")
    suite.addTest(Test002_LoginError, "test_loginerror5")
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = "D:/搜狗高速下载/Python-master/Case/result.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(fp, "测试报告", "用例执行情况：")
    runner.run(suite)
    fp.close()